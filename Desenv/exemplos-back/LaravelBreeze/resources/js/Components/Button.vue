<template>
    <button :type="type" class="inline-flex items-center px-4 py-2 bg-primary-600 border border-transparent rounded-sm font-semibold text-xs text-white uppercase tracking-widest hover:bg-gray-500  transition ease-in-out duration-150">
        <slot />
    </button>
</template>

<script>
export default {
    props: {
        type: {
            type: String,
            default: 'submit',
        },
    }
}
</script>
