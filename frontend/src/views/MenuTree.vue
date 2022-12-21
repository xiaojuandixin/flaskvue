<template>
    <div>
      <el-menu
        default-active
        background-color="#545c64"
        text-color="#fff"
        active-text-color="#ffd04b"
        unique-opened
      >
        <template v-for="(item) in menuList">
          <el-submenu v-if="item.child&&item.child.length>0" :key="item.id" :index="item.id">
            <template slot="title">
              <i class="el-icon-location"></i>
              <span>{{item.name}}</span>
            </template>
            <menu-sun :menuList="item.child"/> 
          </el-submenu>
          <el-menu-item v-else :key="item.id" :index="item.id">{{item.name}}</el-menu-item>
        </template>
      </el-menu>
    </div>
  </template>
  
  <script>
  import MenuSun from "@/components/menuList.vue";
  export default {
    name: "MenuSun",//必须要 递归组件的关键，并且要与引入组件的变量名称一致
    components: {
      MenuSun
    },
    props: {
      menuList: {}  // 菜单的数据
    }
  };
  </script>
  
  