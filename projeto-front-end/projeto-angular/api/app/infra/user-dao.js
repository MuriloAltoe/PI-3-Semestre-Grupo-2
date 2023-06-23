const userConverter = row => ({
    id: row.user_id,
    nome: row.nome,
    email: row.email,
    senha: row.senha,
    tipo: row.tipo,
    cep: row.cep,
    rua: row.rua,
    numero: row.numero,
    bairro: row.bairro,
    cidade: row.cidade,
    estado: row.estado,
    complemento: row.complemento,
    telefone: row.telefone,
    entrega: row.entrega
});

class UserDao {

    constructor(db) {
        this._db = db;
    }

    findByNameAndPassword(userName, password) {
        return new Promise((resolve, reject) => this._db.get(
            `SELECT * FROM user WHERE email = ? AND senha = ?`,
            [userName, password],
            (err, row) => {
                if (err) {
                    console.log(err);
                    return reject('Can`t find user');
                }
                 
                if(row) resolve(userConverter(row));
                resolve(null);
            }
        ));
    }

    findByName(userName) {

        return new Promise((resolve, reject) => this._db.get(
            `SELECT * FROM user WHERE email = ?`,
            [userName],
            (err, row) => {
                if (err) {
                    console.log(err);
                    return reject('Can`t find user');
                }
                if(row) resolve(userConverter(row));
                resolve(null);
            }
        ));
        
    }

    findAll() {
        return new Promise((resolve, reject) => this._db.all(
            `SELECT * FROM user`,
            (err, row) => {
                if (err) {
                    console.log(err);
                    return reject('Can`t find user');
                }
                if(row) resolve(row);
                resolve(null);
            }
        ));
    }

    add(user) {
        return new Promise((resolve, reject) => {
            
            this._db.run(`
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
                ) values (?,?,?,?,?,?,?,?,?,?,?,?,?)
            `,
                [
                    user.nome,
                    user.email,
                    user.senha, 
                    user.tipo,
                    user.cep,
                    user.rua,
                    user.numero,
                    user.bairro,
                    user.cidade,
                    user.estado,
                    user.complemento,
                    user.telefone,
                    user.entrega
                ],
                function (err) {
                    if (err) {
                        console.log(err);
                        return reject('Can`t register new user');
                    }
                    console.log(`User ${user.email} registered!`)
                    resolve();
                });
        });
    }

}
module.exports = UserDao;