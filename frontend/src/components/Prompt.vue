<!-- To do -->
<template>
    <div class="flex ml-auto">
      <router-link to="/login">
        <button class="bg-white hover:bg-slate-400 text-black text-l font-bold p-2 mt-2 mr-2 rounded">Login</button>
      </router-link>
      <router-link to="/register">
        <button class="bg-white hover:bg-slate-400 text-black text-l font-bold p-2 mt-2 mr-2 rounded">Register</button>
      </router-link>
    </div>
    <div class="text-white h-full items-center justify-center flex mb-20">
      <div class="text-center">
        <h1 class="text-xl font-bold mb-4">What do you want to do?</h1>
        <button class="bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
          Start a new project
        </button>
      </div>
    </div>
</template>

<script setup>
// Alot to do
</script>