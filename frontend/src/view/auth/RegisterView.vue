<template>
    <div>
        <AuthHeader></AuthHeader>
        <b-container class="bv-example-row">
            <b-row>
                <b-col>1 of 3</b-col>
                <b-col>
                    <b-form @submit="onSubmit" @reset="onReset" v-if="show">
                        <b-form-group id="input-group-1" label="Email address:" label-for="input-1"
                            description="We'll never share your email with anyone else.">
                            <b-form-input id="input-1" v-model="form.user_mail" type="email" placeholder="Enter email"
                                required></b-form-input>
                        </b-form-group>

                        <b-form-group id="input-group-2" label="Your Password:" label-for="input-2">
                            <b-form-input id="input-2" type="password" v-model="form.password"
                                placeholder="Enter password" required></b-form-input>
                        </b-form-group>

                        <b-form-group id="input-group-3" label="Re Type Password:" label-for="input-3">
                            <b-form-input id="input-3" type="text" v-model="form.re_password"
                                placeholder="Re-Enter password" required></b-form-input>
                        </b-form-group>

                        <b-form-group id="input-group-4" label="Select Role:" label-for="input-4">
                            <b-form-select id="input-4" v-model="form.role" :options="roles" required></b-form-select>
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
                re_password: '',
                role: null,
            },
            roles: [{ text: 'Select One', value: null }, { text: 'Watcher', value: 'watcher' }, { text: 'Admin', value: 'admin' }],
            show: true
        }
    },
    components: {
        AuthHeader
    },
    methods: {
        onSubmit(event) {
                event.preventDefault()
                console.log(this.form.email, this.form.password, this.form.re_password)
                if (!this.form.user_mail || !this.form.password || !this.form.re_password) {
                    alert("Please enter all the fields");
                    return;
                }
                if (!this.form.role) {
                    alert("Please select role");
                    return;
                }
                if (this.form.password != this.form.re_password) {
                    alert("Passwords don't match!!");
                    return;
                }

                axios.post("http://127.0.0.1:8081/api/register", {
                    user_mail: this.form.user_mail,
                    password: this.form.password,
                    role: this.form.role
                }).then((response) => {
                    console.log(response)
                    if (response.data.status == "success") {

                        this.flashMessage.success({
                            message: "Successfully registered, Login please."
                        })

                        this.$router.push("/login");
                    }
                    if (response.data.status == "failed") {
                        // alert(response.data.message);
                        this.onReset();
                    }
                }).catch((error) => {
                    console.error(error);
                    this.flashMessage.error({
                            message: "An error occurred while registering the user"
                        })
                })
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