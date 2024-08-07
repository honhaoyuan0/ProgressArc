<!-- This correspond to the side bar that contains all the project user created -->
<template>
  <div class="text-white h-full w-[260px]">
    <div class="p-4 flex-grow">
      <h2 class="text-3xl font-bold mb-4">Projects</h2>
      <div v-if="projects.length === 0" class="flex items-center h-full">
        <p class="text-center">No projects available. Please add a project to get started!</p>
      </div>
      <ul v-else>
        <li v-for="(project, index) in projects" :key="index" class="mb-2">
            <!-- CRUD function to be determine -->
          <button @click="goToProject(project.id)" class="w-full text-left p-2 hover:bg-gray-700 rounded"> 
            {{ project.name }}
          </button>
        </li>
      </ul>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
    projects: {
        type: Array,
        required: true
    }
})

const goToProject = () => {
//   To do
};
</script>