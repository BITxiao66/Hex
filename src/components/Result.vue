 <template>
  <div class="info">
    <el-row><input type="text" placeholder=".                                  还想听些什么？"  :class="'log-input'" v-model="keywords">
    <el-button type="danger" @click="logout" >搜索</el-button>
    </el-row>
    <el-table
      :data="tableData" 
      style="width: 75%;"
      align="center"> 
      <el-table-column
        prop="date"
        label="日期"
        width="180">
      </el-table-column>
      <el-table-column
        prop="name"
        label="姓名"
        width="180">
      </el-table-column>
      <el-table-column
        prop="address"
        label="地址">
      </el-table-column>
    </el-table>
    <a href @click="logout">[注销]</a>
  </div>
  </template>

  <style>
  .info{background: #fff; width: 100%; height: 600px; color: #2c3e50; text-align: center; padding-top: 170px;align: right;}

  .log-input{width: 370px;overflow: hidden; padding: 0 15px;font-size: 13px; border: 1px solid #EBEBEB; margin:0 auto 15px; height: 36px; line-height: 36px; -webkit-border-radius: 5px;
-moz-border-radius: 5px;
-ms-border-radius: 5px;
-o-border-radius: 5px;
border-radius: 5px;text-align: middle;}
    .el-menu-vertical-demo:not(.el-menu--collapse) {
      width: 200px;
      min-height: 400px;
     }
  </style>

  <script>
    export default {
      data() {
        return {
          tableData: [{
            date: '2016-05-02',
            name: '王小虎',
            address: '上海市普陀区金沙江路 1518 弄'
          }, {
            date: '2016-05-04',
            name: '王小虎',
            address: '上海市普陀区金沙江路 1517 弄'
          }, {
            date: '2016-05-01',
            name: '王小虎',
            address: '上海市普陀区金沙江路 1519 弄'
          }, {
            date: '2016-05-03',
            name: '王小虎',
            address: '上海市普陀区金沙江路 1516 弄'
          }]
        }
      },
      methods: {
        handleOpen(key, keyPath) {
          console.log(key, keyPath);
        },
        handleClose(key, keyPath) {
          console.log(key, keyPath);
        },
        logout(){
      //删除cookie并跳到登录页
      this.delCookie('session');

      //演示
      setTimeout(()=>{
        this.$router.push('/login');
      },3000)
    }
      }
    }
  </script>
