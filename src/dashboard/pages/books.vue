<template>
    <b-container fluid="lg">
        <b-form-row>
            <b-col col lg="10">
                <b-form-input id="input-search" class="mb-2 mr-sm-2 mb-sm-0" placeholder="Search..."> </b-form-input>
            </b-col>

            <b-col cols="12" xs="auto" lg="2">
                <b-button variant="primary" v-b-modal.modal-book>Add Book</b-button>
            </b-col>
        </b-form-row>

        <b-row> </b-row>

        <b-modal id="modal-book" title="Add Book">
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
                        no-wheel="true"
                        required
                    ></b-form-input>
                </b-form-group>

                <b-form-group>
                    <treeselect :options="authors" placeholder="Select your author..." v-model="modal.author" />
                    <treeselect-value :value="modal.author" />
                </b-form-group>
            </b-form>
        </b-modal>
    </b-container>
</template>

<script>
// import the component
import Treeselect from '@riophae/vue-treeselect';
// import the styles
import '@riophae/vue-treeselect/dist/vue-treeselect.css';

export default {
    name: 'books',
    components: { Treeselect },
    data() {
        return {
            authors: [
                { id: 1, label: 'Aaren' },
                { id: 2, label: 'Aarika' },
                { id: 3, label: 'Abagael' },
                { id: 4, label: 'Abagail' },
                { id: 5, label: 'Abbe' },
                { id: 6, label: 'Abbey' },
                { id: 7, label: 'Abbi' },
                { id: 8, label: 'Abbie' },
                { id: 9, label: 'Abby' },
                { id: 10, label: 'Abbye' },
                { id: 11, label: 'Abigael' },
                { id: 12, label: 'Abigail' },
                { id: 13, label: 'Abigale' },
            ],

            books: [],
            modal: {
                name: '',
                author: '',
                pageNumbers: 0,
            },
        };
    },
    methods: {},
};
</script>
