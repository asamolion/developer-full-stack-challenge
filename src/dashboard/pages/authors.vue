<template>
    <b-container fluid="lg">
        <h1>Authors</h1>
        <b-form-row>
            <b-col col lg="10">
                <b-form-input
                    id="input-search"
                    class="mb-2 mr-sm-2 mb-sm-0"
                    placeholder="Search..."
                    v-model="searchQuery"
                ></b-form-input>
            </b-col>

            <b-col cols="12" xs="auto" lg="2">
                <b-button variant="primary" v-b-modal.modal-author>Add Author</b-button>
            </b-col>
        </b-form-row>

        <b-row class="mt-3">
            <b-table :items="authors" per-page="limit" :fields="['name', 'book_count']"></b-table>
            <b-pagination-nav
                v-model="page"
                base-url="/authors?page="
                :number-of-pages="10"
                use-router
            ></b-pagination-nav>
        </b-row>

        <b-modal id="modal-author" title="Create Author" @ok="handleOk">
            <b-form>
                <b-form-group id="form-group-name" label="Name" label-for="input-name">
                    <b-form-input
                        id="input-name"
                        v-model="modal.name"
                        type="text"
                        placeholder="Author name..."
                        required
                    ></b-form-input>
                </b-form-group>
            </b-form>
        </b-modal>
    </b-container>
</template>

<script>
export default {
    name: 'authors',
    data() {
        return {
            searchQuery: this.$route.query.searchQuery ? this.$route.query.searchQuery : '',
            page: this.$route.query.page ? this.$route.query.page : 1,
            authors: [],
            modal: {
                name,
            },
        };
    },
    async fetch() {
        this.getAuthors();
    },
    watch: {
        searchQuery: function () {
            // this could use a debounce
            this.getAuthors();
        },
        page: function () {
            this.$nuxt.refresh();
        },
    },
    methods: {
        handleOk(evt) {
            // Prevent modal from closing
            evt.preventDefault();
            this.addAuthor();
        },
        async getAuthors() {
            this.authors = await this.$axios.$get('/authors', {
                params: { skip: this.page * 10 - 10, limit: 10, search: this.searchQuery },
            });
        },
        async addAuthor() {
            if (this.modal.name === '') {
                alert('Please enter author name.');
                return;
            }
            await this.$axios.$post('/authors', {
                name: this.modal.name,
            });
            this.$nuxt.refresh();
        },
        linkGen() {
            return this.page === 1 ? '/authors' : `/authors?page=${this.page}`;
        },
    },
};
</script>
