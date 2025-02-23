<!-- Login component -->
<template>
  <div class="flex min-h-full flex-1 flex-col justify-center px-6 py-12 lg:px-8 bg-gray-400">
    <div class="sm:mx-auto sm:w-full sm:max-w-sm">
      <img class="mb-10 size-15" src="https://64.media.tumblr.com/c78f81fea60668f04193ad03b8104a9e/c4d7e7ace63a8a3c-1e/s1280x1920/a44175b4c168279d82f7795e7fa3665f455eec82.jpg" />
      <img class="mx-auto h-10 w-auto" src="https://cdn-icons-png.flaticon.com/512/1/1560.png" alt="[LOGO TODO]" />
      <h2 class="mt-10 text-center text-2xl font-bold leading-9 tracking-tight text-gray-900">Sign in to your account</h2>
    </div>
    <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
      <form class="space-y-6">
        <div>
          <label for="email" class="block text-sm font-medium leading-6 text-gray-900">Email address</label>
          <div class="mt-2">
            <input v-model="email" id="email" name="email" type="email" autocomplete="email" required="True" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-gray-600 sm:text-sm sm:leading-6" />
          </div>
        </div>

        <div>
          <div class="flex items-center justify-between">
            <label for="password" class="block text-sm font-medium leading-6 text-gray-900">Password</label>
            <div class="text-sm">
              <a href="#" class="font-semibold text-gray-600 hover:text-gray-500">Forgot password?</a>
            </div>
          </div>
          <div class="mt-2">
            <input v-model='password' id="password" name="password" type="password" autocomplete="current-password" required="True" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-gray-600 sm:text-sm sm:leading-6" />
          </div>
        </div>

        <div>
          <button @click.prevent="HandleLogin" class="flex w-full justify-center rounded-md bg-gray-900 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-gray-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-gray-600">Sign in</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';
import { useAuthStore } from '@/stores/auth';

const email = ref('')
const password = ref('')
const router = useRouter();
const authStore = useAuthStore();

const HandleLogin = async () => {
  // To do
  try {
    const response = await axios.post('http://localhost:5000/login', {
      email: email.value,
      password: password.value
    });
    if (response.status === 200) {
      const data = response.data;
      if (data.status === 'success') {
        authStore.setLoginStatus(true, data.user);
        router.push({
          name: 'Home',
          params: {
            user: data.user
          }
        });
      }
    }
  } catch (error) {
    console.error(error);
    alert('Wrong email or password. Please try again later.');
  }
};
</script>