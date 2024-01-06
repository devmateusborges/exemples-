<template>
    <Head title="Log in" />

    <AppValidationErrors class="mb-4" />

    <div v-if="status" class="mb-4 font-medium text-sm text-green-600">
        {{ status }}
    </div>

    <form  @submit.prevent="submit">
        <div>
            <AppLabel for="email" value="Email" />
            <AppInput id="email" type="email" class="mt-1 block w-full" v-model="form.email" required autofocus autocomplete="username" />
        </div>

        <div class="mt-4">
            <AppLabel for="password" value="Password" />
            <AppInput id="password" type="password" class="mt-1 block w-full" v-model="form.password" required autocomplete="current-password" />
        </div>

        <div class="block mt-4">
            <label class="flex items-center">
                <AppCheckbox name="remember" v-model:checked="form.remember" />
                <span class="ml-2 text-sm text-gray-600">Remember me</span>
            </label>
        </div>

        <div class="flex items-center justify-end mt-4">
            <Link v-if="canResetPassword" :href="route('password.request')" class="underline text-sm text-gray-600 hover:text-gray-900">
                Forgot your password?
            </Link>

            <AppButton class="ml-4" :class="{ 'opacity-25': form.processing }" :disabled="form.processing">
                Log in
            </AppButton>
        </div>
    </form>
</template>

<script>
import AppButton from '@/Components/Button.vue'
import AppCheckbox from '@/Components/Checkbox.vue'
import AppGuestLayout from '@/Layouts/Guest.vue'
import AppInput from '@/Components/Input.vue'
import AppLabel from '@/Components/Label.vue'
import AppValidationErrors from '@/Components/ValidationErrors.vue'
import { Head, Link } from '@inertiajs/inertia-vue3';

export default {
    layout: AppGuestLayout,

    components: {
        AppButton,
        AppCheckbox,
        AppInput,
        AppLabel,
        AppValidationErrors,
        Head,
        Link,
    },

    props: {
        canResetPassword: Boolean,
        status: String,
    },

    data() {
        return {
            form: this.$inertia.form({
                email: '',
                password: '',
                remember: false
            })
        }
    },

    methods: {
        submit() {
            this.form.post(this.route('login'), {
                onFinish: () => this.form.reset('password'),
            })
        }
    }
}
</script>
