<template>
<div class="leftMenu">
<el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect">
  <el-menu-item index="1" >登陆界面</el-menu-item>
  <el-menu-item index="2" >返回搜索界面</el-menu-item>
  <el-menu-item index="3" >退出当前帐号</el-menu-item>
</el-menu>
</div>
</template>

<style>
  .el-menu-vertical-demo:not(.el-menu--collapse) {
    width: 200px;
    min-height: 400px;
  }
  .leftMenu{
    background-color:#EA0000;
  }	
</style>

<script>
  export default {
    data() {
      return {
        activeIndex: '1'
      };
    },
    methods: {
      handleOpen(key, keyPath) {
        console.log(key, keyPath);
      },
      login(){

      },
      searching(){

      },
      logout(){

      }
    }
  }
</script>