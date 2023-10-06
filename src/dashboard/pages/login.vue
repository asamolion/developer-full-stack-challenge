<template>
    <b-container>
        <b-form @submit="onSubmit">
            <b-form-group id="input-group-username" label="Username:" label-for="input-username">
                <b-form-input
                    id="input-username"
                    v-model="form.username"
                    type="text"
                    placeholder="Enter username"
                    required
                ></b-form-input>
            </b-form-group>

            <b-form-group id="input-group-password" label="Password:" label-for="input-password">
                <b-form-input
                    id="input-password"
                    v-model="form.password"
                    type="password"
                    placeholder="Enter password"
                    required
                ></b-form-input>
            </b-form-group>

            <b-button type="submit" variant="primary">Submit</b-button>
        </b-form>
    </b-container>
</template>

<script>
export default {
    auth: false,
    data() {
        return {
            form: {
                username: '',
                password: '',
            },
        };
    },
    methods: {
        async onSubmit(event) {
            event.preventDefault();

            // URLSearchParams used to enable application/x-www-form-urlencoded form request
            const data = new URLSearchParams({
                username: event.target.elements['input-username'].value,
                password: event.target.elements['input-password'].value,
            });

            const response = await this.$auth.loginWith('local', {
                data,
            });
        },
    },
};
</script>
