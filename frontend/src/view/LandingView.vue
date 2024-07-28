<template>
    <div>
<AuthHeader></AuthHeader>
        <div class="container text-center">
            <div class="row">
                <div class="col-2">

                </div>
                <div class="col-8">
                    <div class="container text-center">
                        <div class="row">
                            <div class="col">
                                <router-link to="/login"><b-button variant="outline-primary">Login Page</b-button></router-link>
                            </div>
                            <div class="col">
                                <router-link to="/register"><b-button variant="outline-primary">Register page</b-button></router-link>
                                
                            </div>

                            
                        </div>
                    </div>
                </div>
                <div class="col-2">
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import AuthHeader from '@/components/AuthHeader.vue';

export default {
    name: "LandingPage",
    components:{
        AuthHeader
    }
}

</script>

<style scoped></style>