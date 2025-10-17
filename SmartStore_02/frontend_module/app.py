from flask import Flask, render_template, jsonify, request, redirect, url_for
import json
import os
import time
import random

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

# Mock data
PRODUCTS = [
    {
        'id': '1',
        'name': '智能矿泉水',
        'price': 3.50,
        'originalPrice': 4.00,
        'category': 'beverages',
        'image': '矿泉水',
        'description': '纯净天然矿泉水，智能包装，品质保证',
        'stock': 150,
        'sold': 45,
        'rating': 4.5
    },
    {
        'id': '2',
        'name': '有机薯片',
        'price': 8.90,
        'originalPrice': 10.90,
        'category': 'snacks',
        'image': 'https://via.placeholder.com/300x300/f59e0b/ffffff?text=薯片',
        'description': '精选土豆制作，健康美味零食',
        'stock': 80,
        'sold': 123,
        'rating': 4.2
    },
    {
        'id': '3',
        'name': '智能牙刷',
        'price': 29.90,
        'originalPrice': 39.90,
        'category': 'daily',
        'image': 'https://via.placeholder.com/300x300/10b981/ffffff?text=牙刷',
        'description': 'AI智能感应，全方位清洁护理',
        'stock': 45,
        'sold': 67,
        'rating': 4.8
    },
    {
        'id': '4',
        'name': '无线耳机',
        'price': 199.00,
        'originalPrice': 299.00,
        'category': 'electronics',
        'image': 'https://via.placeholder.com/300x300/8b5cf6/ffffff?text=耳机',
        'description': '高品质音效，长续航无线耳机',
        'stock': 25,
        'sold': 89,
        'rating': 4.6
    },
    {
        'id': '5',
        'name': '功能饮料',
        'price': 6.50,
        'originalPrice': 8.00,
        'category': 'beverages',
        'image': 'https://via.placeholder.com/300x300/ef4444/ffffff?text=饮料',
        'description': '提神醒脑，补充能量',
        'stock': 120,
        'sold': 234,
        'rating': 4.3
    },
    {
        'id': '6',
        'name': '坚果组合',
        'price': 15.90,
        'originalPrice': 18.90,
        'category': 'snacks',
        'image': 'https://via.placeholder.com/300x300/84cc16/ffffff?text=坚果',
        'description': '多种坚果混合，营养丰富',
        'stock': 60,
        'sold': 156,
        'rating': 4.7
    },
    {
        'id': '7',
        'name': '护手霜',
        'price': 12.80,
        'originalPrice': 16.80,
        'category': 'daily',
        'image': 'https://via.placeholder.com/300x300/f97316/ffffff?text=护手霜',
        'description': '滋润保湿，呵护双手',
        'stock': 90,
        'sold': 78,
        'rating': 4.4
    },
    {
        'id': '8',
        'name': '充电宝',
        'price': 89.00,
        'originalPrice': 129.00,
        'category': 'electronics',
        'image': 'https://via.placeholder.com/300x300/6366f1/ffffff?text=充电宝',
        'description': '大容量快充，便携设计',
        'stock': 35,
        'sold': 145,
        'rating': 4.5
    }
]

@app.route('/')
def index():
    return render_template('main/index.html')

@app.route('/demo')
def demo():
    return render_template('main/demo.html')

@app.route('/home')
def home():
    return render_template('main/index.html')

@app.route('/products')
def commodity_list():
    return render_template('main/commodity_list.html')

@app.route('/product/<product_id>')
def commodity_detail(product_id):
    product = next((p for p in PRODUCTS if p['id'] == product_id), None)
    if not product:
        return "Product not found", 404
    return render_template('main/commodity_detail.html', product=product)

@app.route('/user/login')
def login():
    return render_template('user/login.html')

@app.route('/user/member_center')
def member_center():
    return render_template('user/member_center.html')

@app.route('/user/payment')
def payment():
    return render_template('user/payment.html')

@app.route('/admin/admin_login')
def admin_login():
    return render_template('admin/admin_login.html')

@app.route('/admin/inventory_manage')
def inventory_manage():
    return render_template('admin/inventory_manage.html')

@app.route('/admin/order_manage')
def order_manage():
    return render_template('admin/order_manage.html')

# API endpoints
@app.route('/api/products')
def get_products():
    return jsonify(PRODUCTS)

@app.route('/api/products/<product_id>')
def get_product(product_id):
    product = next((p for p in PRODUCTS if p['id'] == product_id), None)
    if not product:
        return jsonify({'error': 'Product not found'}), 404
    return jsonify(product)

@app.route('/api/categories')
def get_categories():
    categories = list(set(p['category'] for p in PRODUCTS))
    return jsonify(categories)

@app.route('/api/login', methods=['POST'])
def login_api():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    method = data.get('method', 'password')
    
    # Mock login logic
    if method == 'password' and username and password:
        return jsonify({
            'success': True,
            'user': {
                'id': '1',
                'username': username,
                'email': f'{username}@example.com',
                'phone': '138****8888',
                'avatar': 'https://via.placeholder.com/100x100/3b82f6/ffffff?text=用户',
                'points': 1280,
                'level': 'VIP会员',
                'membershipLevel': 'silver'
            }
        })
    elif method == 'face':
        return jsonify({
            'success': True,
            'user': {
                'id': '2',
                'username': 'face_user',
                'email': 'face@example.com',
                'phone': '139****9999',
                'avatar': 'https://via.placeholder.com/100x100/10b981/ffffff?text=人脸',
                'points': 2560,
                'level': 'VIP会员',
                'membershipLevel': 'gold'
            }
        })
    return jsonify({'success': False, 'message': 'Invalid credentials'}), 401

@app.route('/api/admin/login', methods=['POST'])
def admin_login_api():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    # Mock admin login logic
    if username == 'admin' and password == 'admin123':
        return jsonify({
            'success': True,
            'admin': {
                'id': 'admin1',
                'username': username,
                'role': 'super_admin',
                'permissions': ['inventory', 'orders', 'users', 'analytics']
            }
        })
    return jsonify({'success': False, 'message': 'Invalid admin credentials'}), 401

@app.route('/api/register', methods=['POST'])
def register_api():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    
    # Mock registration logic
    if username and email and password:
        return jsonify({
            'success': True,
            'user': {
                'id': '3',
                'username': username,
                'email': email,
                'phone': '137****7777',
                'avatar': 'https://via.placeholder.com/100x100/f59e0b/ffffff?text=新用户',
                'points': 100,
                'level': '铜牌会员',
                'membershipLevel': 'bronze'
            },
            'message': '注册成功'
        })
    return jsonify({'success': False, 'message': '注册信息不完整'}), 400

@app.route('/api/orders')
def get_orders():
    orders = [
        {
            'id': '2024123456789',
            'customerName': '张三',
            'customerPhone': '138****8888',
            'total': 45.80,
            'status': '已支付',
            'date': '2024-01-15 14:30:25',
            'items': [
                {'name': '智能矿泉水', 'quantity': 2, 'price': 3.50},
                {'name': '有机薯片', 'quantity': 1, 'price': 8.90}
            ]
        },
        {
            'id': '2024123456790',
            'customerName': '李四',
            'customerPhone': '139****9999',
            'total': 89.90,
            'status': '处理中',
            'date': '2024-01-15 15:45:12',
            'items': [
                {'name': '智能牙刷', 'quantity': 1, 'price': 29.90},
                {'name': '护手霜', 'quantity': 1, 'price': 12.80}
            ]
        }
    ]
    return jsonify(orders)

@app.route('/api/analytics')
def get_analytics():
    analytics = {
        'totalSales': 12847,
        'totalOrders': 156,
        'avgOrderValue': 82.35,
        'conversionRate': 3.2,
        'todayOrders': 23,
        'pendingOrders': 8
    }
    return jsonify(analytics)

# 推荐系统API
@app.route('/api/recommendations/<user_id>')
def get_recommendations_by_user(user_id):
    # 模拟推荐数据
    recommendations = [
        {
            'id': '1',
            'name': '智能矿泉水',
            'price': 3.50,
            'image': 'https://via.placeholder.com/300x300/3b82f6/ffffff?text=矿泉水',
            'reason': '基于您的购买偏好',
            'score': 0.95
        },
        {
            'id': '2',
            'name': '有机薯片',
            'price': 8.90,
            'image': 'https://via.placeholder.com/300x300/f59e0b/ffffff?text=薯片',
            'reason': '相似用户也喜欢',
            'score': 0.87
        },
        {
            'id': '3',
            'name': '智能牙刷',
            'price': 29.90,
            'image': 'https://via.placeholder.com/300x300/10b981/ffffff?text=牙刷',
            'reason': '个性化推荐',
            'score': 0.82
        }
    ]
    return jsonify(recommendations)

@app.route('/api/recommendations/trending')
def get_trending_products():
    trending = [
        {
            'id': '1',
            'name': '智能矿泉水',
            'price': 3.50,
            'image': 'https://via.placeholder.com/300x300/3b82f6/ffffff?text=矿泉水',
            'trendingScore': 0.92
        },
        {
            'id': '4',
            'name': '无线耳机',
            'price': 199.00,
            'image': 'https://via.placeholder.com/300x300/8b5cf6/ffffff?text=耳机',
            'trendingScore': 0.88
        }
    ]
    return jsonify(trending)

# 库存管理API
@app.route('/api/inventory/stats')
def get_inventory_stats():
    stats = {
        'totalProducts': 25,
        'totalValue': 15847.50,
        'lowStockCount': 3,
        'outOfStockCount': 1,
        'overStockCount': 2,
        'activeProducts': 22,
        'averageStock': 45
    }
    return jsonify(stats)

@app.route('/api/inventory/alerts')
def get_inventory_alerts():
    alerts = [
        {
            'id': 'alert_1',
            'type': 'low_stock',
            'productId': '1',
            'productName': '智能矿泉水',
            'currentStock': 8,
            'minStock': 20,
            'message': '商品库存低于最小值',
            'severity': 'warning',
            'createdAt': time.time() * 1000
        },
        {
            'id': 'alert_2',
            'type': 'out_of_stock',
            'productId': '5',
            'productName': '能量饮料',
            'currentStock': 0,
            'minStock': 15,
            'message': '商品已售罄',
            'severity': 'critical',
            'createdAt': time.time() * 1000
        }
    ]
    return jsonify(alerts)

@app.route('/api/inventory/reorder-suggestions')
def get_reorder_suggestions():
    suggestions = [
        {
            'productId': '1',
            'productName': '智能矿泉水',
            'currentStock': 8,
            'minStock': 20,
            'maxStock': 100,
            'suggestedQuantity': 50,
            'estimatedCost': 90.00,
            'supplierId': 'sup_001',
            'priority': 'high'
        },
        {
            'productId': '5',
            'productName': '能量饮料',
            'currentStock': 0,
            'minStock': 15,
            'maxStock': 80,
            'suggestedQuantity': 40,
            'estimatedCost': 104.00,
            'supplierId': 'sup_002',
            'priority': 'urgent'
        }
    ]
    return jsonify(suggestions)

# 用户管理API
@app.route('/api/user/stats/<user_id>')
def get_user_stats(user_id):
    stats = {
        'totalOrders': 45,
        'totalItems': 156,
        'averageOrderValue': 27.79,
        'favoriteHour': 14,
        'membershipDays': 365,
        'pointsThisMonth': 280,
        'favoriteCategory': '饮料'
    }
    return jsonify(stats)

@app.route('/api/user/points-history/<user_id>')
def get_user_points_history(user_id):
    history = [
        {
            'points': 100,
            'reason': '注册奖励',
            'timestamp': time.time() * 1000 - 86400000 * 30,
            'balance': 100
        },
        {
            'points': 35,
            'reason': '购物奖励',
            'timestamp': time.time() * 1000 - 86400000 * 15,
            'balance': 135
        },
        {
            'points': 50,
            'reason': '购物奖励',
            'timestamp': time.time() * 1000 - 86400000 * 7,
            'balance': 185
        }
    ]
    return jsonify(history)

# 支付系统API
@app.route('/api/payment/methods')
def get_payment_methods():
    methods = {
        'face_payment': {
            'name': '人脸支付',
            'icon': '👤',
            'description': '使用人脸识别进行支付',
            'enabled': True,
            'config': {
                'confidenceThreshold': 0.85,
                'livenessCheck': True,
                'antiSpoofing': True
            }
        },
        'qr_payment': {
            'name': '扫码支付',
            'icon': '📱',
            'description': '使用支付宝/微信扫码支付',
            'enabled': True,
            'config': {
                'providers': ['alipay', 'wechat', 'unionpay'],
                'timeout': 300
            }
        },
        'card_payment': {
            'name': '银行卡支付',
            'icon': '💳',
            'description': '使用银行卡进行支付',
            'enabled': True,
            'config': {
                'supportedCards': ['visa', 'mastercard', 'unionpay'],
                'requireCVV': True
            }
        },
        'balance_payment': {
            'name': '余额支付',
            'icon': '💰',
            'description': '使用账户余额支付',
            'enabled': True,
            'config': {
                'requirePassword': True
            }
        }
    }
    return jsonify(methods)

@app.route('/api/payment/create-order', methods=['POST'])
def create_payment_order():
    data = request.get_json()
    order_id = 'order_' + str(int(time.time()))
    
    order = {
        'id': order_id,
        'userId': data.get('userId'),
        'amount': data.get('amount'),
        'currency': data.get('currency', 'CNY'),
        'items': data.get('items', []),
        'status': 'pending',
        'createdAt': time.time() * 1000,
        'expiresAt': (time.time() + 1800) * 1000,  # 30分钟过期
        'paymentMethod': data.get('paymentMethod', 'auto')
    }
    
    return jsonify({
        'success': True,
        'order': order,
        'message': '订单创建成功'
    })

@app.route('/api/payment/process', methods=['POST'])
def process_payment():
    data = request.get_json()
    order_id = data.get('orderId')
    payment_method = data.get('paymentMethod')
    
    # 模拟支付处理
    time.sleep(2)
    
    success = True  # 模拟95%成功率
    if random.random() < 0.05:
        success = False
    
    if success:
        return jsonify({
            'success': True,
            'transactionId': 'txn_' + str(int(time.time())),
            'status': 'completed',
            'completedAt': time.time() * 1000,
            'message': '支付成功'
        })
    else:
        return jsonify({
            'success': False,
            'error': '支付处理失败',
            'message': '请重试或选择其他支付方式'
        }), 400

# 监控面板API
@app.route('/api/dashboard/metrics')
def get_dashboard_metrics():
    metrics = {
        'sales': {
            'todayRevenue': 3847.50,
            'todayOrders': 23,
            'todayItems': 67,
            'avgOrderValue': 167.28,
            'revenueGrowth': 12.5,
            'orderGrowth': 8.3
        },
        'inventory': {
            'totalProducts': 25,
            'lowStockItems': 3,
            'outOfStockItems': 1,
            'inventoryValue': 15847.50,
            'turnoverRate': 2.1
        },
        'users': {
            'activeUsers': 15,
            'newUsersToday': 8,
            'totalUsers': 1247,
            'onlineUsers': 23,
            'conversionRate': 3.2
        },
        'system': {
            'cpuUsage': 23.5,
            'memoryUsage': 67.8,
            'diskUsage': 54.2,
            'networkLatency': 12,
            'uptime': 86400,
            'errorRate': 0.02
        },
        'payments': {
            'totalTransactions': 156,
            'successRate': 97.8,
            'averageProcessingTime': 1.8,
            'failedTransactions': 3,
            'disputedTransactions': 0
        }
    }
    return jsonify(metrics)

@app.route('/api/dashboard/alerts')
def get_dashboard_alerts():
    alerts = [
        {
            'id': 'alert_1',
            'type': 'system',
            'message': 'CPU使用率过高',
            'severity': 'warning',
            'timestamp': time.time() * 1000,
            'status': 'active',
            'acknowledged': False
        },
        {
            'id': 'alert_2',
            'type': 'inventory',
            'message': '发现3个商品库存不足',
            'severity': 'info',
            'timestamp': time.time() * 1000 - 300000,
            'status': 'active',
            'acknowledged': False
        }
    ]
    return jsonify(alerts)

# 实时数据API
@app.route('/api/realtime/sales')
def get_realtime_sales():
    data = {
        'timestamp': time.time() * 1000,
        'revenue': random.randint(200, 800),
        'orders': random.randint(5, 20),
        'items': random.randint(10, 50)
    }
    return jsonify(data)

@app.route('/api/realtime/users')
def get_realtime_users():
    data = {
        'timestamp': time.time() * 1000,
        'onlineUsers': random.randint(15, 35),
        'activeUsers': random.randint(8, 20),
        'newUsers': random.randint(1, 5)
    }
    return jsonify(data)

@app.route('/api/realtime/system')
def get_realtime_system():
    data = {
        'timestamp': time.time() * 1000,
        'cpuUsage': random.uniform(20, 40),
        'memoryUsage': random.uniform(60, 80),
        'diskUsage': random.uniform(50, 70),
        'networkLatency': random.uniform(10, 30)
    }
    return jsonify(data)

@app.route('/api/user/profile')
def get_user_profile():
    user_id = request.args.get('userId')
    # Mock user profile data
    profile = {
        'id': user_id or '1',
        'username': 'test_user',
        'email': 'test@example.com',
        'phone': '138****8888',
        'avatar': 'https://via.placeholder.com/100x100/3b82f6/ffffff?text=用户',
        'points': 1280,
        'membershipLevel': 'silver',
        'totalSpent': 2847.50,
        'orderCount': 15,
        'addresses': [
            {
                'id': 'addr1',
                'name': '张三',
                'phone': '138****8888',
                'province': '北京市',
                'city': '北京市',
                'district': '朝阳区',
                'detail': '科技园A座101室',
                'isDefault': True
            }
        ]
    }
    return jsonify(profile)

@app.route('/api/user/points', methods=['POST'])
def update_points():
    data = request.get_json()
    user_id = data.get('userId')
    points = data.get('points')
    op_type = data.get('type')  # 'add' or 'deduct'
    reason = data.get('reason', '')
    
    # Mock points update
    return jsonify({
        'success': True,
        'newPoints': 1380 if op_type == 'add' else 1180,
        'message': '积分更新成功'
    })

@app.route('/api/user/recommendations')
def get_user_recommendations():
    user_id = request.args.get('userId')
    limit = int(request.args.get('limit', 6))
    
    # Mock recommendations
    recommendations = [
        {
            'id': '6',
            'name': '坚果组合',
            'price': 15.90,
            'image': 'https://via.placeholder.com/300x300/84cc16/ffffff?text=坚果',
            'reason': '根据您的购买历史推荐'
        },
        {
            'id': '7',
            'name': '护手霜',
            'price': 12.80,
            'image': 'https://via.placeholder.com/300x300/f97316/ffffff?text=护手霜',
            'reason': '热销商品'
        },
        {
            'id': '8',
            'name': '充电宝',
            'price': 89.00,
            'image': 'https://via.placeholder.com/300x300/6366f1/ffffff?text=充电宝',
            'reason': '您可能感兴趣'
        }
    ]
    
    return jsonify(recommendations[:limit])

@app.route('/api/payment/process/simple', methods=['POST'])
def process_payment_simple():
    data = request.get_json()
    order_id = data.get('orderId')
    amount = data.get('amount')
    method = data.get('method')
    
    # Mock payment processing
    return jsonify({
        'success': True,
        'transactionId': 'TXN' + str(int(time.time())),
        'message': '支付成功'
    })

@app.route('/api/inventory/analytics')
def get_inventory_analytics():
    analytics = {
        'totalProducts': 156,
        'totalStockValue': 45678.90,
        'totalStockQuantity': 2340,
        'avgStockPerProduct': 15.2,
        'lowStockProducts': 12,
        'outOfStockProducts': 3,
        'stockAlerts': 8
    }
    return jsonify(analytics)

@app.route('/api/inventory/export')
def export_inventory():
    export_format = request.args.get('format', 'csv')
    # Mock export functionality
    return jsonify({
        'success': True,
        'downloadUrl': '/downloads/inventory.' + export_format,
        'message': '导出成功'
    })

@app.route('/api/face/register', methods=['POST'])
def register_face():
    data = request.get_json()
    user_id = data.get('userId')
    face_data = data.get('faceData')
    
    # Mock face registration
    return jsonify({
        'success': True,
        'message': '人脸数据注册成功'
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)