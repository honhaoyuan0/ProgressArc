<template>
    <div class="wrapper" style="--vue3-org-chart-line-color:pink">
        <div class="button-container">
            <button class="text-white" @click="vocApi.zoomReset">Reset Zoom</button>
            <button class="text-white" @click="vocApi.zoomIn">Zoom In</button>
            <button class="text-white" @click="vocApi.zoomOut">Zoom Out</button>
            <button class="text-white" @click="vocApi.expandAll">Expand All</button>
            <button class="text-white" @click="vocApi.collapseAll">Collapse All</button>
            <button class="text-white" @click="vocApi.minimap.toggle">Toggle Minimap</button>
        </div>
      
  
      <div class="chart-container">
        <!-- To test replace the link with components -->
         <!-- https://raw.githubusercontent.com/bumbeishvili/sample-data/main/sample.json -->
        <vue3-org-chart minimap
                        @on-ready="initVue3OrgChart"
                        :json=projectJsonUrl>
          <template #node="{item, children, open, toggleChildren}">
            <div class="node-item justify-center relative" :class="{'active': open, 'passive' : !open }">
              <div class="temp-container">
                <button @click="deleteTask(item.id)" class="absolute top-0 right-0 p-1 hover:bg-gray-200 rounded-full">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-red-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                  </svg>
                </button>
                <div class="text-center">{{item.name}}</div>
                <div class="text-center">{{ item.description }}</div>
                <div class="text-center">{{ item.is_completed }}</div>
                <!-- Pretend there will be a list of sub tasks here -->
                 
                <div class="text-center">Sub Task 1 </div>
                <div v-if="item.is_completed === 'false'" class="flex">
                  <button @click="addSubTask(item.id)" class="mt-2 p-2 bg-blue-500 text-white rounded">Add Sub Task</button>
                  <button @click="markAsCompleted(item.id)" class="mt-2 p-2 bg-green-500 text-white rounded">Mark as Completed</button>
                </div>
                <!-- <div v-else-if="item.is_completed === 'true'" class="flex items-center justify-center mt-2">
                  <div class="p-2 bg-green-500 text-white rounded-full">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                    </svg>
                  </div>
                  <button @click="undoCompletion(item)" class="ml-2 p-2 bg-zinc-700 text-white rounded hover:bg-gray-500">Undo</button>
                </div> -->
                <div v-else class="flex items-center justify-center mt-2">
                  <div class="p-2 bg-green-500 text-white rounded-full">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                    </svg>
                  </div>
                  <button @click="undoCompletion(item)" class="ml-2 p-2 bg-zinc-700 text-white rounded hover:bg-gray-500">Undo</button>
                </div>
                <!-- <div v-else>
                  Cry my guy data is not formatted in to the right format
                </div> -->
              </div>
            </div>
            <div style="text-align: center;">
              <button class="node-btn-toggle" v-if="children.length" @click="toggleChildren" @touchend="toggleChildren">
                {{ open ? '-' : '+' }}
              </button>
            </div>
          </template>
  
          <template #no-data>
            <div style="color:blue; text-align: center;">
              No data
            </div>
          </template>
        </vue3-org-chart>
      </div>
    </div>
  </template>
  
<script setup>
import { onBeforeMount, onMounted, ref } from "vue";
import { useAuthStore } from "@/stores/auth";
import { useProjectStore } from "@/stores/project";
import axios from "axios";

const vocApi = ref(null);
const projectJsonUrl = ref("");

const initVue3OrgChart = ({ api }) => {
  vocApi.value = api;
}
const authStore = useAuthStore();
const projectStore = useProjectStore();

const props = defineProps({
  components: {
    type: Array,
    default: () => []
  },
})

projectJsonUrl.value = `http://localhost:5001/get_project_by_id?user_id=${authStore.user._id}&project_id=${projectStore.project._id}`;

const deleteTask = (taskId) => {
  emit('delete-task', taskId);
};

const addSubTask = (taskId) => {
  emit('add-sub-task', taskId);
};

const markAsCompleted = (taskId) => {
  console.log(projectJsonUrl.value);
  emit('mark-as-completed', taskId);
};

const undoCompletion = (task) => {
  emit('undo-completion', taskId);
};

const updateProject = async () => {
  const payload = {
    user_id: authStore.user._id, // Replace with actual user ID
    project_id: projectStore._id, // Replace with actual project ID
    name: projectStore.name,
    components: props.components
  };
  
  try {
    const response = await axios.post('http://localhost:5001/update_project', payload, {
      headers: {
        'Content-Type': 'application/json'
      }
    });
    console.log("Project updated successfully:", response.data);
  } catch (error) {
    console.error("Error updating project:", error);
  }
};


</script>

<style>
body {
  margin: 0;
  background: #eeeeee;
  height: 100vh;
  overflow: hidden;
}

.wrapper {
  display: flex;
  flex-direction: column;
  height: 100vh;
  width: 100vw;
  padding: 20px;
  box-sizing: border-box;
}

.button-container {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  margin-bottom: 10px;
}

.chart-container {
  flex: 1;
  border: 1px solid #e8e8e8;
  background: white;
  border-radius: 8px;
  overflow: auto;
}

.btn {
  display: block;
  margin: 20px auto;
  padding: 10px 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
  background: #fff;
  cursor: pointer;
  outline: none;
}

.node-item {
  display: flex;
  width: 15rem;
  border-radius: 0.35rem;
  border: 1px solid #e2e8f0;
  padding: 0.5rem;
}

.node-item > :not([hidden]) ~ :not([hidden]) {
  margin-left: 1rem;
}

.node-item:hover {
  background-color: rgb(226 232 240);
}

.node-item.active {
  border-color: rgb(165 180 252);
  background-color: rgb(224 231 255);
}

.node-item.passive {
  background-color: rgb(248 250 252)
}

.node-item .avatar {
  height: 3rem;
  width: 3rem;
  border-radius: 9999px;
}

.node-btn-toggle {
  padding: 1px;
  cursor: pointer;
  height: 1rem;
  width: 1rem;
  border: 1px solid #e2e8f0;
  background-color: rgb(255 255 255);
  font-size: 0.75rem;
  line-height: 10px;
}
</style>