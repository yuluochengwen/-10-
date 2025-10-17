/**
 * SmartStore Dashboard Monitoring
 * 仪表盘实时监控与可视化（占位实现，避免 404）
 */

(function(){
    // Simple no-op initializations to avoid ReferenceErrors if templates call these
    function initCharts(){
        // If ECharts is available and target elements exist, render simple charts
        if (typeof echarts === 'undefined') return;
        const salesEl = document.getElementById('sales-chart');
        if (salesEl) {
            const chart = echarts.init(salesEl);
            chart.setOption({
                title: { text: '销售额趋势', left: 'center', textStyle: { fontSize: 14 } },
                xAxis: { type: 'category', data: ['Mon','Tue','Wed','Thu','Fri','Sat','Sun'] },
                yAxis: { type: 'value' },
                series: [{ type: 'line', data: [120, 200, 150, 80, 70, 110, 130] }]
            });
        }
        const statusEl = document.getElementById('order-status-chart');
        if (statusEl) {
            const chart = echarts.init(statusEl);
            chart.setOption({
                title: { text: '订单状态分布', left: 'center', textStyle: { fontSize: 14 } },
                tooltip: { trigger: 'item' },
                series: [{
                    type: 'pie', radius: '60%',
                    data: [
                        { value: 35, name: '待支付' },
                        { value: 58, name: '已支付' },
                        { value: 22, name: '处理中' },
                        { value: 16, name: '已发货' },
                        { value: 9,  name: '已送达' }
                    ]
                }]
            });
        }
    }

    // Initialize when DOM ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initCharts);
    } else {
        initCharts();
    }
})();
