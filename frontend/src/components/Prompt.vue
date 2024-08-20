<!-- To do -->
<template>
    <div class="text-white h-full items-center justify-center flex">
      <div class="text-center">
        <h1 class="text-xl font-bold mb-4">Welcome {{ user?.email }}</h1>
        <h1 class="text-xl font-bold mb-4">What do you want to do?</h1>
        <button class="bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
          Start a new project
        </button>
      </div>
    </div>
</template>

<script setup>
const props = defineProps({
  user: Object
});
// Alot to do
</script>