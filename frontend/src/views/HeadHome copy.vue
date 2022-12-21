<template>
    <div>
      <el-row>
        <el-col :span="12">
          <el-card>
            <div slot="header" class="clearfix">
              <span>用户信息</span>
            </div>
            <el-form label-width="100px">
              <el-form-item label="用户名">
                <el-input v-model="user.name"></el-input>
              </el-form-item>
              <el-form-item label="邮箱">
                <el-input v-model="user.email"></el-input>
              </el-form-item>
            </el-form>
          </el-card>
        </el-col>
      </el-row>
    </div>
  </template>

<script>
  export default {
    data() {
      return {
        user: {
          name: 'John Doe',
          email: 'john@example.com'
        }
      }
    }
  }
</script>
  