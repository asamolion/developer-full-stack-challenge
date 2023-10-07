<template>
    <b-container fluid="lg">
        <h1>Authors</h1>
        <b-form-row>
            <b-col col lg="10">
                <b-form-input id="input-search" class="mb-2 mr-sm-2 mb-sm-0" placeholder="Search..."></b-form-input>
            </b-col>

            <b-col cols="12" xs="auto" lg="2">
                <b-button variant="primary" v-b-modal.modal-author>Add Author</b-button>
            </b-col>
        </b-form-row>

        <b-row class="mt-3">
            <b-table :items="authors" per-page="limit"></b-table>
            <b-pagination-nav
                v-model="page"
                :link-gen="linkGen"
                :per-page="10"
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
            page: this.$route.query.page ? this.$route.query.page : 1,
            authors: [],
            modal: {
                name,
            },
        };
    },
    async fetch() {
        this.authors = await this.$axios.$get('/authors', {
            params: { skip: this.page * 10 - 10, limit: 10 },
        });
    },
    methods: {
        handleOk(evt) {
            // Prevent modal from closing
            evt.preventDefault();
            this.addAuthor();
        },
        async getAuthors() {
            return await this.$axios.$get('/authors', { params: { skip: this.skip, limit: this.limit } });
        },
        async addAuthor() {
            if (this.modal.name === '') {
                alert('Please enter author name.');
                return;
            }
            const author = await this.$axios.$post('/authors', {
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
