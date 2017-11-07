<template>
 <el-container style="height: 1000px; width: 100%; border: 0px solid #fff;background-color:#fff">
  <el-aside width="300px" style="background-color: rgb(245, 210, 210)">
    <el-tabs type="border-card">
  <el-tab-pane>
    <span slot="label" >热门歌单</span>
      <el-table :data="tablea">
          <el-table-column
          width="210px" >
            <template slot-scope="scope"><a @click="hot(scope.row)">{{scope.row.name}}</a>
            </template>
          </el-table-column>
          <el-table-column
          width="25px">
            <template slot-scope="scope"><a @click="addreal(scope.row)"><i class="el-icon-circle-plus" ></i></a>
            </template>
          </el-table-column>
      </el-table>
  </el-tab-pane>
  <el-tab-pane>
    <span slot="label">个人歌单</span>
    <el-table :data="tableb" @row-click="hot">
          <el-table-column
          prop="name"
          width="250">
          </el-table-column>
          </el-table-column>
        </el-table>
  </el-tab-pane>
</el-tabs>
  </el-aside>

  <el-container width="490px">
   <el-header width="490px" style="text-align: right; font-size: 25px">
      <el-button @click="logout">注销</el-button> 
    </el-header>
  
    
    
    <el-main class="user-info" width="500px" v-loading="loading">
      <div class="user-info">
      <h1 class="nick" style="margin right: 200px;text-align: right" v-if="nottable" >Hello, Xuda</h1></p>
      </div>

      <el-carousel :interval="4000" type="card" height="200px" v-if="nottable">
        <el-carousel-item v-for="item in dataimg" :key="item">
          <img :src="item.url">
        </el-carousel-item>
     </el-carousel>
    
     <el-table :data="tableData" :row-class-name="tableRowClassName" v-if="!nottable">
        <el-table-column prop="song" label="歌曲名" width="140" >
        </el-table-column>
        <el-table-column prop="singer" label="歌手" width="120">
        </el-table-column>
        <el-table-column prop="album" label="专辑">
        </el-table-column>
        <el-table-column
         label="播放"
          width="100">
      <template slot-scope="scope"><a v-bind:href=scope.row.url><i class="el-icon-caret-right" style="margin-right: 45px"></i></a>
      </template>
    </el-table-column>
      </el-table>


    </el-main>

  </el-container>
</el-container>
    
</template>

<style>
  .el-header {
    background-color: #AE0000;
    color: #333;
    line-height: 60px;
  }
  .el-menu-vertical-demo:not(.el-menu--collapse) {
    width: 200px;
    min-height: 400px;
  }
  .el-aside {
    background-color: #FF7575;
    color: #FF7575;
  }
  .portrait{width: 200px; height: 200px; overflow:hidden; -webkit-border-radius: 100%;
-moz-border-radius: 100%;
-ms-border-radius: 100%;
-o-border-radius: 100%; 
border-radius: 100%; background-color: #FF9797; margin:0 auto 15px;border: 2px solid #FF9797; display: block;}

.log-btn{width:402px; display: block; text-align: left; line-height: 50px;margin:0 auto 15px; height:50px; color:#fff; font-size:13px;-webkit-border-radius: 5px; background-color: #3B5999;
-moz-border-radius: 5px;
-ms-border-radius: 5px;
-o-border-radius: 5px;
border-radius: 5px;
position: relative;}
.log-btn.tw{background-color: #13B4E9}
.log-btn.email{background-color: #50E3CE}
.log-btn:hover,.log-btn:focus{color: #fff; opacity: .8;}
.log-input{width: 370px;overflow: hidden; padding: 0 15px;font-size: 13px; border: 1px solid #EBEBEB; margin:0 auto 15px; height: 48px; line-height: 48px; -webkit-border-radius: 5px;
-moz-border-radius: 5px;
-ms-border-radius: 5px;
-o-border-radius: 5px;
border-radius: 5px;}
.log-input.warn{border: 1px solid #f88787}
.info{background: #fff; width: 100%; height: 600px; color: #2c3e50; text-align: center; padding-top: 170px;}
.portrait{width: 200px; height: 200px; overflow:hidden; -webkit-border-radius: 100%;
-moz-border-radius: 100%;
-ms-border-radius: 100%;
-o-border-radius: 100%; 
border-radius: 100%; background-color: #CCCCCC; margin:0 auto 15px;border: 2px solid #2c3e50; display: block;}
.user-info{margin: 38px 0 0 0; vertical-align: top;text-align:center;background-color: #fff;}
.user-info, .w-star, .w-diamond, .nick, .level{display: inline-block;}
.nick{margin-right: 5px;}
.cut{padding: 0 10px; color:#E9E9E9; font-size: 15px;}
.logout{color: #2c3e50; display: block; margin-top: 20px;}

.el-table .warning-row {
    background: #fff;
  }

  .el-table .success-row {
    background: #ffecec;
  } 

.el-carousel__item h3 {
    color: #475669;
    font-size: 14px;
    opacity: 0.75;
    line-height: 200px;
    margin: 0;
  }
  
  .el-carousel__item:nth-child(1) {
    background-color: #99a9bf;
  }
  
  .el-carousel__item:nth-child(2) {
    background-color: #d3dce6;
  }
</style>

<script>
  let fff = 0;
  var tablebfake=[];
  export default {
    data () {
      const item = {
        name: '一如少年模样',
        singer: '陈鸿宇',
        id: '1',
        url: 'http://music.163.com/#/song?id=463157222',
        copyright: '网易云音乐',
        state: '1'
      }
      const item2 = {
        name: '一如少年模样1',
        singer: '陈鸿宇',
        url: 'http://music.163.com/#/song?id=463157222',
        copyright: '网易云音乐',
        state: '0',
        id: '2'
      }
      return {
        nottable: true,
        isCollapse: true,
        dataimg: [{url: require('../images/3.jpg')}, {url: require('../images/1.jpg')}, {url: require('../images/2.jpg')}],
        tablea: [],
        tableb: [],
        tableData: [],
        loading: false
      }
    },
    created()
    {
      this.tojsona();
      //this.tojsonb();
    },
    methods: {
      tojsona()
      {
        var xmlhttp;
        var data=[];
        xmlhttp=new XMLHttpRequest(); 
        xmlhttp.open("GET","http://10.62.47.48:5000/get_list",true);
        xmlhttp.send();
        xmlhttp.onreadystatechange=function()
        {
          if (xmlhttp.readyState==4 && xmlhttp.status==200)
          {
            var jstr=xmlhttp.responseText;
            var jobj=JSON.parse(jstr);
            let count = jobj.count;
            for(let i=0; i<count; i++)
            {
              var s = {};
              s.id = jobj.list_id[i];
              s.name = jobj.list_name[i];
              data[i] = s;
            }
          }
        }
        this.tablea=data;
      }, 
      to()
      {
        this.nottable=true;
      },   
      tojsonb(){
        this.nottable=true;
        var xmlhttp;
        var data=[];
        xmlhttp=new XMLHttpRequest(); 
        xmlhttp.open("GET","http://10.62.47.48:5000/my_list",true);
        xmlhttp.send();
        xmlhttp.onreadystatechange=function()
        {
          if (xmlhttp.readyState==4 && xmlhttp.status==200)
          {
            var jstr=xmlhttp.responseText;
            var jobj=JSON.parse(jstr);
            let count = jobj.count;
            for(let i=0; i<count; i++)
            {
              var s = {};
              s.id = jobj.list_id[i];
              s.name = jobj.list_name[i];
              data[i] = s;
            }
          }
        }
          this.tableb=data;
      },
      tojsontry()
      {
        var data={};
        data={"nameabc" : "lalala"};
        var a=[];
        var b={};
        b.name=data.nameabc;
        a[0]=b;
        this.tablea=a;
      },
      handleOpen (key, keyPath) {
        console.log(key, keyPath)
      },
      handleClose (key, keyPath) {
        console.log(key, keyPath)
      },
      logout() {
      //删除cookie并跳到登录页
      this.delCookie('session');

      //演示
      setTimeout(()=>{
        this.$router.push('/login');
      },1000)
      },
      tableRowClassName({row, rowIndex}) {
        if (row.state === '0\r') {
          return 'warning-row'
        } else if (row.state === '1\r') {
          return 'success-row'
        }
        return ''
      },
      addreal(row){
        var data=[];
        let id=row.id;
        var xmlhttp;
        xmlhttp=new XMLHttpRequest();
        xmlhttp.open("GET","http://10.62.47.48:5000/add_list/"+id,true);
        xmlhttp.send();
        this.tojsonb();
      },
      add(row){
        var data=[];
        var x={};
        data=tablebfake;
        x.id=row.id;
        x.name=row.name;
        data[fff]=x;
        fff=fff+1;
        tablebfake=data;
        this.tableb=tablebfake;   
      },
      hot(row){
        this.nottable=false;
        this.loading=true;
        var data=[];
        let id=row.id;
        var xmlhttp;
        xmlhttp=new XMLHttpRequest();
        xmlhttp.open("GET","http://10.62.47.48:5000/get_song/"+id,true);
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
              obj.song=jobj.song_name[i];         
              obj.singer=jobj.singer[i];
              obj.state=jobj.copyrights[i];
              obj.album=jobj.album[i];
              obj.url=jobj.link[i];
              data[i] = obj;
            }
          }
        }
        this.tableData=data;
        setTimeout(() => {
          this.loading=false;
        }, 2000);
      }
    }
  }
</script>