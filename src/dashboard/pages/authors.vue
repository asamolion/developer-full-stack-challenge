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
            <b-table
                :items="authors"
                per-page="10"
                :fields="['name', 'book_count']"
                @row-clicked="openEditModal"
            ></b-table>
            <b-pagination-nav
                v-model="page"
                base-url="/authors?page="
                :number-of-pages="10"
                use-router
            ></b-pagination-nav>
        </b-row>

        <b-modal
            id="modal-author"
            :title="modal.authorId ? 'Edit Author' : 'Create Author'"
            @ok="handleOk"
            @hidden="resetModal"
            v-model="showModal"
        >
            <b-form-group v-if="modal.authorId" id="form-group-authorid" label="Author ID" label-for="input-authorid">
                <b-form-input
                    id="input-authorid"
                    v-model="modal.authorId"
                    type="number"
                    placeholder="Author ID..."
                    readonly
                ></b-form-input>
            </b-form-group>
            <b-form-group id="form-group-name" label="Name" label-for="input-name">
                <b-form-input
                    id="input-name"
                    v-model="modal.name"
                    type="text"
                    placeholder="Author name..."
                    required
                ></b-form-input>
            </b-form-group>

            <b-form-group v-if="modal.authorId">
                <p>Books</p>
                <b-form-group>
                    <b-form-input
                        id="input-book-name"
                        v-model="modal.bookName"
                        type="text"
                        placeholder="Book name..."
                        required
                    ></b-form-input>
                </b-form-group>
                <b-form-group>
                    <b-form-input
                        id="input-page-numbers"
                        v-model="modal.bookPageNumbers"
                        type="number"
                        min="1"
                        step="1"
                        placeholder="Page numbers..."
                        required
                    ></b-form-input>
                </b-form-group>
                <b-form-group>
                    <b-button variant="primary" @click="addBook">Add Book</b-button>
                </b-form-group>
                <b-table :items="modal.books" :fields="['name', 'page_numbers', 'delete_book']">
                    <template #cell(delete_book)="book">
                        <b-button variant="danger" @click="deleteBook(book.item.id)">Delete</b-button>
                    </template>
                </b-table>
            </b-form-group>
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
            showModal: false,
            modal: {
                authorId: 0,
                name: '',
                bookName: '',
                bookPageNumbers: 0,
                books: [],
            },
        };
    },
    async fetch() {
        this.getAuthors();

        if (this.showModal && this.modal.authorId) {
            this.getBooks();
        }
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
        async handleOk(evt) {
            // Prevent modal from closing
            evt.preventDefault();
            if (this.modal.authorId) {
                await this.editAuthor();
            } else {
                await this.addAuthor();
            }
            this.showModal = false;
        },
        resetModal() {
            this.modal = {
                authorId: 0,
                name: '',
                bookName: '',
                bookPageNumbers: 0,
                books: [],
            };
        },
        openEditModal(author) {
            this.modal.authorId = author.id;
            this.modal.name = author.name;
            this.getBooks();

            this.showModal = true;
        },
        async getBooks() {
            this.modal.books = await this.$axios.$get('/books', {
                params: {
                    author_id: this.modal.authorId ? this.modal.authorId : 0,
                },
            });
        },
        async addBook() {
            if (this.modal.bookName === '') {
                alert('Please enter book name.');
                return;
            }
            if (this.modal.bookPageNumbers <= 0) {
                alert('Please enter valid page numbers.');
                return;
            }
            await this.$axios.$post('/books', {
                name: this.modal.bookName,
                page_numbers: this.modal.bookPageNumbers,
                author_id: this.modal.authorId,
            });
            this.modal.bookName = '';
            this.modal.bookPageNumbers = 0;
            this.getBooks();
        },
        async deleteBook(bookId) {
            const confirmation = confirm('Are you sure?');

            if (confirmation) {
                await this.$axios.$delete(`/books/${bookId}`);
                this.$nuxt.refresh();
            }
        },
        async getAuthors() {
            this.authors = await this.$axios.$get('/authors', {
                params: { skip: this.page * 10 - 10, search: this.searchQuery },
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
        async editAuthor() {
            await this.$axios.$patch(`/authors/${this.modal.authorId}`, {
                name: this.modal.name,
            });
            this.resetModal();
            this.$nuxt.refresh();
        },
    },
};
</script>
