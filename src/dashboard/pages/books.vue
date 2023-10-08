<template>
    <b-container fluid="lg">
        <h1>Books</h1>
        <b-form-row>
            <b-col col lg="10">
                <b-form-input
                    id="input-search"
                    class="mb-2 mr-sm-2 mb-sm-0"
                    placeholder="Search..."
                    v-model="searchQuery"
                >
                </b-form-input>
            </b-col>

            <b-col cols="12" xs="auto" lg="2">
                <b-button variant="primary" v-b-modal.modal-book>Add Book</b-button>
            </b-col>
        </b-form-row>

        <b-row class="mt-3">
            <b-table :items="books" :per-page="10" :fields="['name', 'page_numbers', 'author_name']"></b-table>
            <b-pagination-nav
                v-model="page"
                base-url="/books?page="
                :number-of-pages="10"
                use-router
            ></b-pagination-nav>
        </b-row>

        <b-modal id="modal-book" title="Add Book" @ok="handleOk">
            <b-form>
                <b-form-group
                    id="form-group-name"
                    label="Name"
                    label-for="input-name"
                    description="We'll never share your email with anyone else."
                >
                    <b-form-input
                        id="input-name"
                        v-model="modal.name"
                        type="text"
                        placeholder="Book name..."
                        required
                    ></b-form-input>
                </b-form-group>

                <b-form-group id="input-group-page-numbers" label="Page numbers:" label-for="input-page-numbers">
                    <b-form-input
                        id="input-page-numbers"
                        v-model="modal.pageNumbers"
                        type="number"
                        placeholder="page numbers..."
                        :no-wheel="true"
                        required
                    ></b-form-input>
                </b-form-group>

                <b-form-group>
                    <treeselect
                        :async="true"
                        :options="authors"
                        :load-options="loadAuthors"
                        :auto-load-root-options="false"
                        :normalizer="normalizer"
                        placeholder="Select your author..."
                        v-model="modal.author"
                    />
                </b-form-group>
            </b-form>
        </b-modal>
    </b-container>
</template>

<script>
import Treeselect from '@riophae/vue-treeselect';
import { ASYNC_SEARCH } from '@riophae/vue-treeselect';

import '@riophae/vue-treeselect/dist/vue-treeselect.css';

export default {
    name: 'books',
    components: { treeselect: Treeselect },
    data() {
        return {
            page: this.$route.query.page ? this.$route.query.page : 1,
            searchQuery: this.$route.query.searchQuery ? this.$route.query.searchQuery : '',
            authors: [],
            books: [],
            modal: {
                name: '',
                author: '',
                pageNumbers: 0,
            },
        };
    },
    async fetch() {
        await this.getBooks();
    },
    watch: {
        searchQuery: function (newVal, oldVal) {
            // this could use a debounce
            this.getBooks();
        },
        page: function () {
            this.$nuxt.refresh();
        },
    },

    methods: {
        handleOk(evt) {
            // Prevent modal from closing
            evt.preventDefault();
            this.addBook();
        },
        async getBooks() {
            this.books = await this.$axios.$get('/books', {
                params: { skip: this.page * 10 - 10, search: this.searchQuery },
            });
        },
        async addBook() {
            if (this.modal.name === '') {
                alert('Please enter book name.');
                return;
            }
            if (this.modal.pageNumbers <= 0) {
                alert('Please enter valid page numbers.');
                return;
            }
            if (!this.modal.author) {
                alert('Please select an author.');
                return;
            }
            await this.$axios.$post('/books', {
                name: this.modal.name,
                page_numbers: this.modal.pageNumbers,
                author_id: this.modal.author,
            });
            this.$nuxt.refresh();
        },
        normalizer(author) {
            return { id: author.id, label: author.name };
        },
        loadAuthors: async function ({ action, searchQuery, callback }) {
            if (action === ASYNC_SEARCH) {
                this.authors = await this.$axios.$get('/authors', {
                    params: { skip: this.page * 10 - 10, search: searchQuery },
                });

                callback(null, this.authors);
            }
        },
    },
};
</script>
