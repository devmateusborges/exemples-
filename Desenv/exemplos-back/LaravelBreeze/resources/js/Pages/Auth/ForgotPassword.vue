<template>
    <Head title="Forgot Password" />

    <div class="mb-4 text-sm text-gray-600">
        Forgot your password? No problem. Just let us know your email address and we will email you a password reset link that will allow you to choose a new one.
    </div>

    <div v-if="status" class="mb-4 font-medium text-sm text-green-600">
        {{ status }}
    </div>

    <AppValidationErrors class="mb-4" />

    <form @submit.prevent="submit">
        <div>
            <AppLabel for="email" value="Email" />
            <AppInput id="email" type="email" class="mt-1 block w-full" v-model="form.email" required autofocus autocomplete="username" />
        </div>

        <div class="flex items-center justify-end mt-4">
            <AppButton :class="{ 'opacity-25': form.processing }" :disabled="form.processing">
                Email Password Reset Link
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
import { Head } from '@inertiajs/inertia-vue3';

export default {
    layout: AppGuestLayout,

    components: {
        AppButton,
        AppInput,
        AppLabel,
        AppValidationErrors,
        Head,
    },

    props: {
        status: String,
    },

    data() {
        return {
            form: this.$inertia.form({
                email: ''
            })
        }
    },

    methods: {
        submit() {
            this.form.post(this.route('password.email'))
        }
    }
}
</script>
