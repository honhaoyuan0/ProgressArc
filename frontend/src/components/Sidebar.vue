<!-- This correspond to the side bar that contains all the project user created -->
<template>
  <div class="text-white h-full w-[260px]">
    <div class="p-4 flex-grow">
      <h2 class="text-3xl font-bold mb-4">Projects</h2>
      <div v-if="projects.length === 0" class="flex items-center justify-center h-full">
        <p class="text-center">No projects available. Please start a project</p>
      </div>
      <ul v-else>
        <li v-for="(project, index) in projects" :key="index" class="mb-2 flex">
            <!-- CRUD function to be determine -->
          <button @mousedown="goToProject(project)"
                  @keydown.enter="handleEnterKey($event, project)"
                  class="w-full text-left p-2 hover:bg-gray-700 rounded text-lg" 
                  style="word-break: break-word;">
            <div  :ref="el => projectNameRefs[index] = el"
                  :contenteditable="editingIndex === index" 
                  @blur="updateProjectName(project._id, $event)" >      
              {{ project.name }}
            </div>
          </button>
          <!-- Edit button -->
          <button @click="startEditing(index)" class="text-white-500 p-2 hover:text-white">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.232 5.232l3.536 3.536M9 11l6 6M4 21h7l-7-7v7z" />
            </svg>
          </button>
          <!-- Delete button -->
          <button @click="deleteProject(index)" class="text-white-500 p-2 hover:text-red-700">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 6h18M9 6v12m6-12v12M4 6l1-1h14l1 1M5 6h14v14H5z" />
            </svg>
          </button>
        </li>
      </ul>
    </div>
  </div>
</template>

<script setup>
import { useAuthStore } from '@/stores/auth';
import { useProjectStore } from '@/stores/project';
import { ref, nextTick} from 'vue';

const props = defineProps({
  projects: {
      type: Array,
      default: () => []
  },
})
const authStore = useAuthStore();
const projectStore = useProjectStore();
const emit = defineEmits(['selectProjects', 'deleteProject', 'updateProjectName']);
const editingIndex = ref(null);
const projectNameRefs = ref([]);

const goToProject = (project) => {
  projectStore.setProject(project);
  emit('selectProjects', {components: project.components});
};

const deleteProject = async (index) => {
  try {
    const deleteUrl = `http://localhost:5001/delete_project?user_id=${authStore.user._id}&project_id=${props.projects[index]._id}`;
    const response = await fetch(deleteUrl, {
      method: 'DELETE',
    });
    const data = await response.json();
    console.log(data);
    authStore.updateUser(data.user);
    console.log("Delete project button pressed");
    emit('deleteProject', {projects: data.user.projects});
  } catch (error) {
    console.error(error);
  }
};

const startEditing = async (index) => {
  editingIndex.value = index;
  await nextTick();
  const projectNameElement = projectNameRefs.value[index];
  if (projectNameElement) {
    projectNameElement.focus();
  }
  else {
    console.error("Project name element not found");
  }
  // console.log("Edit project name button pressed");
}

const handleEnterKey = (event, project) => {
  if (event.shiftKey) {
    // Allow Shift+Enter to add a newline
    event.stopPropagation();
  } else {
    // Trigger goToProject on Enter key
    event.preventDefault();
    goToProject(project);
  }
};

const updateProjectName = async (project_id, event) => {
  try {
    const newName = event.target.innerText.trim();
    const response = await fetch(`http://localhost:5001/update_project_name`, {
      method: 'PATCH',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ user_id: authStore.user._id, project_id: project_id, new_name: newName })
    });
    const data = await response.json();
    console.log(data);
    authStore.updateUser(data.user);
    emit('updateProjectName', {projects: data.user.projects});
  } catch (error) {
    console.error(error);
  }
}
</script>