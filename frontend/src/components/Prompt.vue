<!-- To do -->
<template>
    <div class="text-white h-full items-center justify-center flex">
      <div class="text-center">
        <h1 class="text-xl font-bold mb-4">Welcome {{ user?.email }}</h1>
        <h1 class="text-xl font-bold mb-4">What do you want to do?</h1>
        <button @click="createProject" class="bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
          Start a new project
        </button>
      </div>
    </div>
</template>

<script setup>
import { ref, watchEffect } from 'vue';
import { useAuthStore } from '@/stores/auth';
import { useProjectStore } from '@/stores/project';

const props = defineProps({
  user: Object
});
const authStore = useAuthStore();
const projectStore = useProjectStore();
const root_component = ref([
  {
    "name": "New Task",
    "tasks": "Type in your task description here",
    "is_completed": "false",
    "id": "1",
    "parentId": "",
    "size": ""
  }
]);
const payload = {
  "_id": "",
  "name": "New Project",
  "components": root_component.value
}
const emit = defineEmits(['updateProjectList']);

watchEffect(() => {
  if (props.user && props.user._id) {
    payload._id = props.user._id;
  }
});

const createProject = async () => {
  try {
    const response = await fetch('http://localhost:5001/create_project', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(payload)
    });

    const data = await response.json();
    console.log(data);
    // After successfully adding a project, update user in the authStore
    authStore.updateUser(data.user);
    projectStore.setProject(data.project);
    emit('updateProjectList', { components: data.project.components, projects: data.user.projects });
  } catch (error) {
    console.error(error);
  }
}
</script>