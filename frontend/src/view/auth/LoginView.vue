<template>
    <div>
        <AuthHeader></AuthHeader>
        <b-container class="bv-example-row">
            <b-row>
                <b-col>1 of 3</b-col>
                <b-col>
                    <b-form @submit="onSubmit" @reset="onReset" v-if="show">
                        <b-form-group id="input-group-1" label="Email address:" label-for="input-1">
                            <b-form-input id="input-1" v-model="form.user_mail" type="email" placeholder="Enter email"
                                required></b-form-input>
                        </b-form-group>

                        <b-form-group id="input-group-2" label="Your Password:" label-for="input-2">
                            <b-form-input id="input-2" type="password" v-model="form.password"
                                placeholder="Enter password"></b-form-input>
                        </b-form-group>

                        <b-button type="submit" variant="primary">Submit</b-button>
                        <b-button type="reset" variant="danger">Reset</b-button>
                    </b-form>
                    <b-card class="mt-3" header="Form Data Result">
                        <pre class="m-0">{{ form }}</pre>
                    </b-card>
                </b-col>
                <b-col>3 of 3</b-col>
            </b-row>
        </b-container>

    </div>
</template>

<script>

import AuthHeader from '@/components/AuthHeader.vue';
import axios from 'axios'
export default {
    data() {
        return {
            form: {
                user_mail: '',
                password: '',
            },
            show: true
        }
    },
    components: {
        AuthHeader
    },
    methods: {
        onSubmit(event) {
            event.preventDefault()
            if (!this.form.user_mail || !this.form.password) {
                this.flashMessage.error({
                    message: "Please eneter email and password"
                })
                return;
            }

            axios.post("http://127.0.0.1:8081/api/login", {
                user_mail: this.form.user_mail,
                password: this.form.password
            })
                .then((response) => {
                    console.log(response)
                    if (response.data.status === "sucess") {

                        this.$store.dispatch("set_state_after_login", response.data);

                        this.flashMessage.success({
                            message: response.data.message
                        })

                        this.$router.push("/");
                    }
                    if (response.data.status === "failed") {
                        this.flashMessage.error({
                            message: response.data.message
                        })
                    }
                }).catch((error) => {
                    console.error(error);
                    // alert("An error occurred while login the user")
                    this.flashMessage.error({
                        message: "Error occur will login the user"
                    })
                }
                )
        },


        onReset(event) {
            event.preventDefault()
            // Reset our form values
            this.form.user_mail = ''
            this.form.password = ''
            this.form.re_password = ''
            this.form.role = null
            // Trick to reset/clear native browser form validation state
            this.show = false
            this.$nextTick(() => {
                this.show = true
            })
        }
    }
}
</script>

<style scoped></style>








v-if 
v-for 
v-model
v-bind
@submit or v-click="submit"