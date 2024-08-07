<!-- Register component -->
<template>
  <div class="flex min-h-full flex-1 flex-col justify-center px-6 py-12 lg:px-8">
    <div class="sm:mx-auto sm:w-full sm:max-w-sm">
      <img class="mx-auto h-10 w-auto" src="https://tailwindui.com/img/logos/mark.svg?color=indigo&shade=600" alt="Your Company" />
      <h2 class="mt-10 text-center text-2xl font-bold leading-9 tracking-tight text-gray-900">Sign up an account</h2>
    </div>

    <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
      <!-- action="#" method="POST" -->
      <form class="space-y-6">
        <!-- Email box -->
        <div>
          <label for="email" class="block text-sm font-medium leading-6 text-gray-900">Email address</label>
          <div class="mt-2">
            <input v-model="email" id="email" name="email" type="email" autocomplete="email" required="True" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
          </div>
        </div>
        <!-- Password Box -->
        <div>
          <div class="flex items-center justify-between">
            <label for="password" class="block text-sm font-medium leading-6 text-gray-900">Password</label>
          </div>
          <div class="mt-2">
            <input v-model='password' id="password" name="password" type="password" autocomplete="current-password" required="True" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
          </div>
        </div>
        <!-- Confirm Password Box -->
        <div>
          <div class="flex items-center justify-between">
            <label for="password" class="block text-sm font-medium leading-6 text-gray-900">Confirm Password</label>
          </div>
          <div class="mt-2">
            <input v-model='confirm_password' id="confirm_password" name="password" type="password" autocomplete="current-password" required="True" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
          </div>
        </div>
        <!-- Sign Up Button -->
        <div>
          <button @click.prevent="handleRegister" class="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Sign Up</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';

const email = ref('')
const password = ref('')
const confirm_password = ref('')
const isLoggedIn = ref(false)

const handleRegister = async () => {
  // To do
  if (password.value !== confirm_password.value) {
    alert('Passwords do not match');
    return;
  }

  try {
    const response = await axios.post('http://localhost:5000/register', {
      email: email.value,
      password: password.value,
      confirm_password: confirm_password.value
    }, {
      headers: {
        'Content-Type': 'application/json'
      }
    });
    console.log(response.data.message);
    // Additional logic for the data
    // <route to="/login" />;
  } catch (error) {
    console.error(error);
  }
};
</script>