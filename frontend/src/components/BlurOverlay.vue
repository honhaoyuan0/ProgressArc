<template>
  <div class="fixed inset-0 flex items-center justify-center bg-gray-800 bg-opacity-100 z-50">
    <div class="text-center">
      <h1 class="text-2xl text-white mb-4">Please log in or sign up to access our website. &#x1F60A;</h1>
      <div class="flex space-x-4 justify-center">
        <router-link to="/login">
          <button class="bg-gray-700 hover:bg-gray-600 text-white font-bold py-2 px-4 rounded">Login</button>
        </router-link>
        <router-link to="/register">
          <button class="bg-black hover:bg-gray-900 text-white font-bold py-2 px-4 rounded">Sign Up</button>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script setup>
</script>