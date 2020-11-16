<template>
<div class="test">
    <!-- axios test -->
  <button>调用表型信息表格</button>
  <button v-on:click="getPhenotypeClusterAssoInfo">调用表型关联细胞cluster柱状图</button>
  <p>{{echartsDataCategory}}</p>
  <div id="main" style="width: 100%;height:400px;">
  </div>
</div>
</template>

<script>
import Vue from 'vue';
import echarts from 'echarts';
import VCharts from 'v-charts';
Vue.use(VCharts);
// For axios
import axios from 'axios/dist/axios.min';

export default{
  // 监听axios传递过来的echartsData，若存在值的变化则再次执行
  watch: {
    echartsData() {
      this.getPhenotypeClusterAssoInfoEcharts();
    }
  }, 
  data() {
    return {
      echartsData: [], 
      echartsDataIndex: [],
      echartsDataCategory: [],
      test_data: [
                    ['score', 'amount', 'product'],
                    [89.3, 58212, 'Matcha Latte'],
                    [57.1, 78254, 'Milk Tea'],
                    [74.4, 41032, 'Cheese Cocoa'],
                    [50.1, 12755, 'Cheese Brownie'],
                    [89.7, 20145, 'Matcha Cocoa'],
                    [68.1, 79146, 'Tea'],
                    [19.6, 91852, 'Orange Juice'],
                    [10.6, 101852, 'Lemon Juice'],
                    [32.7, 20112, 'Walnut Brownie']
                ], 
      fuck_data: [ [ "p_value", "id", "cell", "organ", "source", "p_value_log" ], [ "0.7321824939691397", "SRA709816_SRS3331832.14", "Unknown", "Unknown", "ES-derived kidney organoid", 0.13538065904297547 ], [ "0.9996338888222567", "SRA709816_SRS3331832.15", "Unknown", "Unknown", "ES-derived kidney organoid", 0.0001590291772133547 ], [ "0.8791018999496274", "SRA709816_SRS3331832.16", "Unknown", "Unknown", "ES-derived kidney organoid", 0.055960781330239476 ], [ "0.7205519623220376", "SRA749327_SRS3693908.11", "Unknown", "Unknown", "Merkel Cell Carcinoma", 0.14233469474450283 ], [ "0.06117263225207226", "SRA709816_SRS3331832.17", "Macrophages", "Immune/Blood system", "ES-derived kidney organoid", 1.2134428314532468 ], [ "0.9957435600072354", "SRA749327_SRS3693908.10", "Unknown", "Unknown", "Merkel Cell Carcinoma", 0.0018524937183988812 ], [ "0.9538449815646951", "SRA709816_SRS3331832.10", "Unknown", "Unknown", "ES-derived kidney organoid", 0.020522200894913075 ], [ "0.8276810983114795", "SRA709816_SRS3331832.11", "Unknown", "Unknown", "ES-derived kidney organoid", 0.08213696263702908 ], [ "0.838278732763688", "SRA709816_SRS3331832.12", "Unknown", "Unknown", "ES-derived kidney organoid", 0.07661155180685307 ] ]
    }
  }, 
  mounted() {
    this.getPhenotypeClusterAssoInfoEcharts(); // 调用绘图渲染方法
  },
  methods:{
    //门店营收数据
    getMerchantSelling() {
        // 调用数据api获取数据
        this.getPhenotypeClusterAssoInfo();
        // 基于准备好的dom，获取main节点init初始化echarts实例
        var myChart = echarts.init(document.getElementById('main'));
        // 指定图表的配置项和数据
        var option = {
            dataset: {
                source: this.echartsData
            },
            xAxis: {
              type: 'category'
            },
            yAxis: {
              type: 'value'
            },
            series: [
                {
                    type: 'bar',
                    encode: {
                        // 将 "amount" 列映射到 X 轴。
                        x: 'id',
                        // 将 "product" 列映射到 Y 轴。
                        y: 'p_value_log'
                    }
                }
            ]
        };
        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option);
      },
    // 细胞系log转换后p-value信息
    getPhenotypeClusterAssoInfoEcharts() {

      // 基于准备好的dom，初始化echarts实例
      var myChart = echarts.init(document.getElementById('main'));
      var option = {
          // 数据获取
          dataset: {
              source: this.echartsData
          },
          // Axis属性调整
          xAxis: {
            type: 'category'
          },
          yAxis: {
            type: 'value'
          },
          // 视觉元素映射
          visualMap: [
            {
              type: 'piecewise', 
              dimension: 'organ',
              categories: this.echartsDataCategory, 
              orient: 'horizontal', 
              inRange: {
                // ["#2F9323","#D9B63A","#2E2AA4","#9F2E61","#4D670C","#BF675F","#1F814A","#357F88","#673509","#310937","#1B9637","#F7393C"]
                color: gradient
              }
            }
          ],
          // 加入工具箱
          toolbox: {
              feature: {
                  dataZoom: {
                      yAxisIndex: 'none'
                  },
                  restore: {},
                  saveAsImage: {}
              }
          },
          // 加入交互组件
          dataZoom: [{
              type: 'inside',
              start: 0,
              end: 5
          }, {
              start: 0,
              end: 5,
              handleIcon: 'M10.7,11.9v-1.3H9.3v1.3c-4.9,0.3-8.8,4.4-8.8,9.4c0,5,3.9,9.1,8.8,9.4v1.3h1.3v-1.3c4.9-0.3,8.8-4.4,8.8-9.4C19.5,16.3,15.6,12.2,10.7,11.9z M13.3,24.4H6.7V23h6.6V24.4z M13.3,19.6H6.7v-1.4h6.6V19.6z',
              handleSize: '80%',
              handleStyle: {
                  color: '#fff',
                  shadowBlur: 3,
                  shadowColor: 'rgba(0, 0, 0, 0.6)',
                  shadowOffsetX: 2,
                  shadowOffsetY: 2
              }
          }],
          // 图形绘制
          series: [
              {
                  type: 'bar',
                  encode: {
                      // 将 "amount" 列映射到 X 轴。
                      x: 'id',
                      // 将 "product" 列映射到 Y 轴。
                      y: 'p_value_log'
                  }
              }
          ]
      };
    // 显示动态加载动画
    if(this.echartsData.length == 0){
      myChart.showLoading();
    }else{
      myChart.hideLoading();
    }
    myChart.setOption(option);
    }, 
    getPhenotypeClusterAssoInfo: function () {
    // 获取进程中的变量信息
    var _this=this;
    // axios实现异步请求以获取get命令后的返回结果
    axios.get('http://localhost/test/json_api_single_query_demo.php', {
      params:{
        query:'phenotype',
        species:'hs', 
        query_info:'phenotype_cluster_asso',
        query_value:'Nealelab_id_111'
      }
    })  // 获取返回结果后进行处理
        .then(function (response) {
            // 将返回结果转为json格式，第一行作为列名
            var jsonObj = JSON.parse(JSON.stringify(response.data));
            // 添加p_value_log数据
            // 添加'p_value_log'进入index信息
            jsonObj[0].push('p_value_log');
            // 获取p_value所在index
            var p_value_index = jsonObj[0].indexOf('p_value');
            var p_value_log_index = jsonObj[0].indexOf('p_value_log');
            for (let i = 1; i < jsonObj.length; i++){
              jsonObj[i].push(-(Math.log10(jsonObj[i][p_value_index])));
            }
            // 根据p_value_log的值进行从大到小排序
            jsonObj = jsonObj.sort((a,b)=>b[p_value_log_index]-a[p_value_log_index]);

            _this.echartsData = jsonObj;
            _this.echartsDataIndex = jsonObj[0];

            // 获取视觉映射所需category信息
            // 获取organ所在index
            var organ_index = _this.echartsDataIndex.indexOf('organ');
            // 遍历获取所有category信息并传入集合中
            let all_category = new Set();
            for (let i = 1; i < _this.echartsData.length; i++){
              all_category.add(_this.echartsData[i][organ_index]);
            }
            
            _this.echartsDataCategory = Array.from(all_category);
        })
        .catch(function (error) {
            console.log(error);
        });
    },
  }
}

</script>
