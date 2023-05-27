const sqlite3 = require('sqlite3').verbose();
const db = new sqlite3.Database('data.db');

const USER_SCHEMA = `
CREATE TABLE IF NOT EXISTS user (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT, 
    nome VARCHAR(30) NOT NULL, 
    email VARCHAR(255) NOT NULL UNIQUE, 
    senha VARCAHR(255) NOT NULL,
    tipo VARCAHR(40) NOT NULL, 
    cep VARCAHR(255) NOT NULL,
    rua VARCAHR(255) NOT NULL,
    numero INTERGER NOT NULL,
    bairro VARCAHR(255) NOT NULL,
    cidade VARCAHR(255) NOT NULL,
    estado VARCAHR(255) NOT NULL,
    complemento VARCAHR(255),
    telefone VARCAHR(255),
    entrega VARCAHR(255)
)
`;

const INSERT_DEFAULT_USER_1 = 
`
INSERT INTO user (
    nome,
    email,
    senha,
    tipo,
    cep,
    rua,
    numero,
    bairro,
    cidade,
    estado,
    complemento,
    telefone,
    entrega
) SELECT 'Witer Mendonça', 'witer@gmail.com', '12345678', 'produtor','13606-336', 'Augusta Viola', 893, 'jd Celina', 'Araras', 'SP', 'ap 304, bloco 37','019911991188', 'true' WHERE NOT EXISTS (SELECT * FROM user WHERE email = 'witer@gmail.com')
`;

const INSERT_DEFAULT_USER_2 = 
`
INSERT INTO user (
    nome,
    email,
    senha,
    tipo,
    cep,
    rua,
    numero,
    bairro,
    cidade,
    estado,
    complemento,
    telefone,
    entrega
) SELECT 'Ester', 'ester@gmail.com', '12345678', 'consumidor','13606-336', 'Augusta Viola', 893, 'jd Celina', 'Araras', 'SP', 'ap 304, bloco 37','019911991188', 'true' WHERE NOT EXISTS (SELECT * FROM user WHERE email = 'ester@gmail.com')
`;


db.serialize(() => {
    db.run("PRAGMA foreign_keys=ON");
    db.run(USER_SCHEMA);
    db.run(INSERT_DEFAULT_USER_1);
    db.run(INSERT_DEFAULT_USER_2);       

    db.each("SELECT * FROM user", (err, user) => {
        console.log('Users');
        console.log(user);
    });
});

process.on('SIGINT', () =>
    db.close(() => {
        console.log('Database closed');
        process.exit(0);
    })
);

module.exports = db;