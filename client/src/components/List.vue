<template>
    <div class="container">
        <div class="row">
            <div class="col">
                <table class="table table-light">
                    <thead>
                        <tr>
                            <th scope="col">Fecha</th>
                            <th>Folio</th>
                            <th scope="col">Remitente</th>
                            <th scope="col">Adscripcion</th>
                            <th scope="col">Asunto</th>
                            <th scope="col">Hora</th>
                            <th scope="col"># Hojas</th>
                            <th scope="col">Anexos</th>
                            <th scope="col">Derivado</th>
                            <th scope="col">Observaciones</th>
                            <th scope="col">Operaciones</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="dt in data" :key="dt[0]">
                            <td>{{ dt[1] }}</td>
                            <td>{{ dt[2] }}</td>
                            <td>{{ dt[3] }}</td>
                            <td>{{ dt[4] }}</td>
                            <td>{{ dt[5] }}</td>
                            <td>{{ dt[6] }}</td>
                            <td>{{ dt[7] }}</td>
                            <td>{{ dt[8] }}</td>
                            <td>{{ dt[9] }}</td>
                            <td>{{ dt[10] }}</td>
                            <td>
                                <a href="#" class="btn btn-secondary">Actualizar</a>
                                <a href="#" class="btn btn-danger">Eliminar</a>
                            </td>
                        </tr>
                        
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'List',
    data() {
        return {
            data: [],
        };
    },
    methods: {
        getList() {
            const path = 'http://localhost:5000/list';
            axios.get(path)
              .then((res) => {
                this.data = res.data.results;
              })
              .catch((error) => {
                console.log(error);
              });
        },
    },
    created(){
        this.getList();
    },
};
</script>