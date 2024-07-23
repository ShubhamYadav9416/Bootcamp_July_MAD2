<template>
    <div>
        <div class="container text-center">
            <div class="row">
                <div class="col-2">

                </div>
                <div class="col-8">
                Login page
                <HelloWorld></HelloWorld>
                </div>
                <div class="col-2">
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import HelloWorld from '@/components/HelloWorld.vue';

export default {
    name: "LoginPage",
    components: {
        HelloWorld
    }
}

</script>

<style scoped></style>