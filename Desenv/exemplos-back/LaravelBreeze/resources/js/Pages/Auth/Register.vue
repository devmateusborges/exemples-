<template>
    <Head title="Register" />

    <AppValidationErrors class="mb-4" />

    <form @submit.prevent="submit">
        <div>
            <AppLabel for="name" value="Name" />
            <AppInput id="name" type="text" class="mt-1 block w-full" v-model="form.name" required autofocus autocomplete="name" />
        </div>

        <div class="mt-4">
            <AppLabel for="email" value="Email" />
            <AppInput id="email" type="email" class="mt-1 block w-full" v-model="form.email" required autocomplete="username" />
        </div>

        <div class="mt-4">
            <AppLabel for="password" value="Password" />
            <AppInput id="password" type="password" class="mt-1 block w-full" v-model="form.password" required autocomplete="new-password" />
        </div>

        <div class="mt-4">
            <AppLabel for="password_confirmation" value="Confirm Password" />
            <AppInput id="password_confirmation" type="password" class="mt-1 block w-full" v-model="form.password_confirmation" required autocomplete="new-password" />
        </div>

        <div class="flex items-center justify-end mt-4">
            <Link :href="route('login')" class="underline text-sm text-gray-600 hover:text-gray-900">
                Already registered?
            </Link>

            <AppButton class="ml-4" :class="{ 'opacity-25': form.processing }" :disabled="form.processing">
                Register
            </AppButton>
        </div>
    </form>
</template>

<script>
import AppButton from '@/Components/Button.vue'
import AppGuestLayout from '@/Layouts/Guest.vue'
import AppInput from '@/Components/Input.vue'
import AppLabel from '@/Components/Label.vue'
import AppValidationErrors from '@/Components/ValidationErrors.vue'
import { Head, Link } from '@inertiajs/inertia-vue3';

export default {
    layout: AppGuestLayout,

    components: {
        AppButton,
        AppInput,
        AppLabel,
        AppValidationErrors,
        Head,
        Link,
    },

    data() {
        return {
            form: this.$inertia.form({
                name: '',
                email: '',
                password: '',
                password_confirmation: '',
                terms: false,
            })
        }
    },

    methods: {
        submit() {
            this.form.post(this.route('register'), {
                onFinish: () => this.form.reset('password', 'password_confirmation'),
            })
        }
    }
}
</script>
