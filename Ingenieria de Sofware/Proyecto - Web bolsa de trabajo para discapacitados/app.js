const express = require('express');
const mysql = require('mysql');
const cors = require('cors');

const bodyParser = require('body-parser');

const PORT = process.env.PORT || 3050;

const app = express();

app.use(cors());
app.use(bodyParser.json());

/* MySQL */

 var connection = mysql.createConnection({
    host     : 'localhost',//host     : '23.102.173.84',
    user     : 'ingenieria',
    password : 'is-escom123!',
    database : 'discapacidad',
    multipleStatements: true
  }); 

/* var connection = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: '',
    database: 'discapacidad',
    multipleStatements: true
}); */

// Fin MySQL

//Route
app.get('/', (req, res) => {
    res.send("Bienvenido a mi API!");
});

//Obtener todos los empleos
app.get('/empleos', (req, res) => {
    const sql = `SELECT p.*, d.nombre as 'discapacidad', e.nombre as 'empresa', e.email FROM puesto p, 
    discapacidad d, dis_pue dp, empresa e WHERE e.rfc=p.rfc_empresa AND p.id_puesto = dp.id_puesto AND 
    dp.id_discapacidad=d.id_discapacidad ORDER BY 1`;

    connection.query(sql, (error, results) => {
        if (error) throw error;
        if (results.length > 0) {
            res.json(results);
        } else {
            res.send('No tenemos resultados');
        }
    });
});

/* Obtener empleo por ID */
app.get('/empleos/:id', (req, res) => {
    const { id } = req.params;
    const sql = `SELECT * FROM puesto WHERE id_puesto = ${id}`;
    connection.query(sql, (error, results) => {
        if (error) throw error;
        if (results.length > 0) {
            res.json(results);
        } else {
            res.send('No tenemos resultados');
        }
    });
});

/* Obtener empleo por discapacidad y sueldo */
app.get('/empleos/:id/:sueldo', (req, res) => {
    const { id, sueldo } = req.params;
    const sql = `SELECT p.*, d.nombre as 'discapacidad', e.nombre as 'empresa', e.email FROM puesto p, 
    discapacidad d, dis_pue dp, empresa e WHERE e.rfc=p.rfc_empresa AND p.id_puesto = dp.id_puesto AND 
    dp.id_discapacidad=d.id_discapacidad AND d.id_discapacidad = ${id} AND p.salario_mes > ${sueldo} GROUP BY 1;`;


    connection.query(sql, (error, results) => {
        if (error) throw error;
        if (results.length > 0) {
            res.json(results);
        } else {
            res.send('No tenemos resultados');
        }
    });
});

/* Agregar Empleo */
app.post('/agregarEmpleo', (req, res) => {
    const sql = "INSERT INTO puesto SET ?;SELECT id_puesto FROM puesto ORDER BY id_puesto DESC";

    const puestoObject = {
        titulo: req.body.titulo,
        palabras_clave: req.body.palabras_clave,
        salario_mes: req.body.salario_mes,
        requisitos: req.body.requisitos,
        descripcion: req.body.descripcion,
        zona_trabajo: req.body.zona_trabajo,
        rfc_empresa: req.body.rfc_empresa
    }


    connection.query(sql, puestoObject, (error, results) => {
        if (error)
            throw error;
        else {
            const sql = "INSERT INTO dis_pue SET ?";
            const datosTablaDis_Pue = {
                id_discapacidad: req.body.discapacidad,
                id_puesto: results[1][0].id_puesto
            };
            connection.query(sql, datosTablaDis_Pue, error => {
                if (error) {
                    throw error;
                }
                else
                    res.send('Empleo creado!');
            });
        }
    });

});

/* Actualizar Empleo */
app.put('/actualizarEmpleo/:id', (req, res) => {
    const { id } = req.params;
    const {
        titulo,
        palabras_clave,
        salario_mes,
        requisitos,
        descripcion,
        zona_trabajo,
        rfc_empresa
    } = req.body;
    const sql = `UPDATE puesto SET titulo = '${titulo}', palabras_clave = '${palabras_clave}',
            salario_mes = ${salario_mes}, requisitos = '${requisitos}', descripcion = '${descripcion}',
            zona_trabajo = '${zona_trabajo}', rfc_empresa = '${rfc_empresa}'
             WHERE id_puesto = ${id}`;

    connection.query(sql, error => {
        if (error)
            throw error;
        else
            res.send('Empleo actualizado!');
    });
});

/* Borrar Empleo */
app.delete('/borrarEmpleo/:id', (req, res) => {
    const { id } = req.params;
    const sql = `DELETE FROM puesto WHERE id_puesto = ${id}`;

    connection.query(sql, error => {
        if (error)
            throw error;
        else
            res.send('Empleo eliminado!');
    });
});

//Check connect
connection.connect(error => {
    if (error) throw error;
    console.log("Base de datos corriendo exitosamente");
});

//

app.listen(PORT, () => console.log(`Server running on port ${PORT}`));