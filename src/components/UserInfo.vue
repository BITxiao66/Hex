//用户信息

<template>
<transition name="fade">
<div class="info">
	<img class="portrait" :src="$store.state.userInfo.portrait" width="200" height="200" />

	<div class="user-info">
			<h1 class="nick" v-text="'Hello, ' + $store.state.userInfo.nick"></h1>
      </p>
      <input type="text" placeholder=".                                  今天你想听什么？"  :class="'log-input'" v-model="keywords">
      <a href="javascript:;" class="log-btn" @click="searching" v-if="!issearching">搜索</a>
			<a href="javascript:;" class="logout" @click="logout" v-if="!isLogouting"> [注销]</a>
	</div>
  <Loading v-if="isLogouting" marginTop="3%"></Loading>
</div>
</transition>
</template>
<script>
import Loading from './Loading.vue'
export default {
  name: 'UserInfo',
  data(){
  	return {
      isLogouting: false,
      issearching: false
    }
  },
  components:{
    Loading
  },
  computed: {
  	levelClass(){
  		var level = this.level;
  		if (1 <= level && level <= 7) {
        	return 1;
      	} else if (8 <= level && level <= 16) {
        	return 2;
      	} else if (16 <= level && level <= 31) {
        	return 3;
      	} else if (32 <= level && level <= 63) {
        	return 4;
      	} else if (64 <= level && level <= 127) {
          	return 5;
      	} else if (128 <= level && level <= 254) {
        	return 6;
      	} else {
        	return 6;
      	}
  	}
  },
  methods: {
    //注销
    logout(){
      //删除cookie并跳到登录页
      this.isLogouting = true;
      this.delCookie('session');

      //演示
      setTimeout(()=>{
        this.$router.push('/login');
        this.isLogouting = false;
      },3000)
    },
    searching(){
        this.issearching = true;
        this.isLogouting = true;

      setTimeout(()=>{
        this.$router.push('/result/');
        this.issearching = false;
        this.isLogouting = false;
      },3000)
    }
  }
}
</script>

<style scoped>
.info{background: #fff; width: 100%; height: 600px; color: #2c3e50; text-align: center; padding-top: 170px;}
.portrait{width: 200px; height: 200px; overflow:hidden; -webkit-border-radius: 100%;
-moz-border-radius: 100%;
-ms-border-radius: 100%;
-o-border-radius: 100%; 
border-radius: 100%; background-color: #CCCCCC; margin:0 auto 15px;border: 2px solid #2c3e50; display: block;}
.user-info{margin: 38px 0 0 0; vertical-align: top;}
.log-input{width: 370px;overflow: hidden; padding: 0 15px;font-size: 13px; border: 1px solid #EBEBEB; margin:0 auto 15px; height: 48px; line-height: 48px; -webkit-border-radius: 5px;
-moz-border-radius: 5px;
-ms-border-radius: 5px;
-o-border-radius: 5px;
border-radius: 5px;}
.user-info, .w-star, .w-diamond, .nick, .level{display: inline-block;}
.nick{margin-right: 10px;}
.cut{padding: 0 10px; color:#E9E9E9; font-size: 15px;}
.logout{color: #2c3e50; display: block; margin-top: 20px;}
.log-btn{width:402px; display: block; text-align: middle; line-height: 50px;margin:0 auto 15px; height:50px; color:#fff; font-size:13px;-webkit-border-radius: 5px; background-color: #EA0000 !important;
-moz-border-radius: 5px;
-ms-border-radius: 5px;
-o-border-radius: 5px;
border-radius: 5px;
position: relative;}
.log-btn .icons{margin-left: 30px; vertical-align: middle;}
.log-btn.tw{background-color: #13B4E9}
.log-btn.email{background-color: #50E3CE}
.log-btn:hover,.log-btn:focus{color: #fff; opacity: .8;}
.log-btn.text{left: 95px; line-height: 50px; text-align: left; position: absolute;}
</style>
