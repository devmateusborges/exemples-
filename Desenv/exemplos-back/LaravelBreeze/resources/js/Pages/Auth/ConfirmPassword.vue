<template>
    <Head title="Confirm Password" />

    <div class="mb-4 text-sm text-gray-600">
        This is a secure area of the application. Please confirm your password before continuing.
    </div>

    <AppValidationErrors class="mb-4" />

    <form @submit.prevent="submit">
        <div>
            <AppLabel for="password" value="Password" />
            <AppInput id="password" type="password" class="mt-1 block w-full" v-model="form.password" required autocomplete="current-password" autofocus />
        </div>

        <div class="flex justify-end mt-4">
            <AppButton class="ml-4" :class="{ 'opacity-25': form.processing }" :disabled="form.processing">
                Confirm
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

    data() {
        return {
            form: this.$inertia.form({
                password: '',
            })
        }
    },

    methods: {
        submit() {
            this.form.post(this.route('password.confirm'), {
                onFinish: () => this.form.reset(),
            })
        }
    }
}
</script>
