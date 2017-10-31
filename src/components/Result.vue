 <template>
  <div class="info">
    <el-row><input type="text" placeholder=".                                  还想听些什么？"  :class="'log-input'" >
    <el-button type="danger" @click="logout" >搜索</el-button>
    </el-row>
    <el-table
      :data="tableData" 
      style="width: 75%;"
      id="result-table"
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
    created()
    {
       this.tojsontry();
    },
    data() {
      return{
      tableData: []
      }
    },
    methods: {
      tojson()
      {
          var data=[];
          var obj={
          "address": "New One 639", 
          "date": "20171029", 
          "name": "xuda"
        }
        data[0]=obj;
          this.tableData=data;
      },

        tojsontry()
        {
          var data=[];
          //alert('obj.date');
        var xmlhttp;
        xmlhttp=new XMLHttpRequest();
        xmlhttp.open("POST","http://10.62.62.150:5000/json_test",true);
        xmlhttp.send();
        xmlhttp.onreadystatechange=function()
        {       
          if ((xmlhttp.readyState==4 && xmlhttp.status==200 ))
          {
            var jstr=xmlhttp.responseText;

            var jobj=JSON.parse(jstr);
            let count=jobj.count;
            for(let i=0; i< count;i++)
            {
              var obj={};
              obj.date=jobj.date[i];         
              obj.name=jobj.name[i];
              obj.address=jobj.address[i];
              data[i] = obj;
            }
          }
        }
        this.tableData=data;
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
  