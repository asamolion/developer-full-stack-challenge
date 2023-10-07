<template>
    <div>
        <b-navbar toggleable="lg" type="dark" variant="warning">
            <b-navbar-brand to="/">DataCose</b-navbar-brand>

            <b-nav pills>
                <b-nav-item to="/" exact exact-active-class="active">Home</b-nav-item>
                <b-nav-item v-if="!$auth.loggedIn" to="/login" exact exact-active-class="active">Login</b-nav-item>
                <b-nav-item v-if="$auth.loggedIn" to="/books" exact exact-active-class="active">Books</b-nav-item>
                <b-nav-item v-if="$auth.loggedIn" to="/authors" exact exact-active-class="active">Authors</b-nav-item>
            </b-nav>
        </b-navbar>
        <Nuxt class="mt-3" />
    </div>
</template>

<style scoped></style>
