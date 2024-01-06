<template>
    <Head title="Reset Password" />

    <AppValidationErrors class="mb-4" />

    <form @submit.prevent="submit">
        <div>
            <AppLabel for="email" value="Email" />
            <AppInput id="email" type="email" class="mt-1 block w-full" v-model="form.email" required autofocus autocomplete="username" />
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
            <AppButton :class="{ 'opacity-25': form.processing }" :disabled="form.processing">
                Reset Password
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
        email: String,
        token: String,
    },

    data() {
        return {
            form: this.$inertia.form({
                token: this.token,
                email: this.email,
                password: '',
                password_confirmation: '',
            })
        }
    },

    methods: {
        submit() {
            this.form.post(this.route('password.update'), {
                onFinish: () => this.form.reset('password', 'password_confirmation'),
            })
        }
    }
}
</script>
