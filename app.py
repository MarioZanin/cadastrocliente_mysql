from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_smorest import Api, Blueprint, abort as smorest_abort
from flask.views import MethodView
from flask_cors import CORS
from config import Config
from marshmallow import Schema, fields, ValidationError
from flask import send_from_directory # executar com html

# --- INICIALIZAÇÃO sem o tml---
# app = Flask(__name__)
app = Flask(__name__, static_folder="static", static_url_path="/static")
app.config.from_object(Config)
CORS(app)

db = SQLAlchemy()
db.init_app(app)

api = Api(app)
blp = Blueprint("clientes", __name__, url_prefix="/clientes", description="Operações em Clientes")


# --- MODELO ---
class ClienteModel(db.Model):
    __tablename__ = "cliente"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(14), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True)
    telefone = db.Column(db.String(20))
    endereco = db.Column(db.String(255))


# --- SCHEMA (simples e funcional) ---
class ClienteSchema(Schema):
    id = fields.Int(dump_only=True)
    nome = fields.Str(required=True)
    cpf = fields.Str(required=True)
    email = fields.Str(allow_none=True)
    telefone = fields.Str(allow_none=True)
    endereco = fields.Str(allow_none=True)


cliente_schema = ClienteSchema()
clientes_schema = ClienteSchema(many=True)

# Criar tabelas
with app.app_context():
    db.create_all()


# --- ENDPOINTS ---


@blp.route("/")
class ClienteList(MethodView):

    @blp.response(200, clientes_schema)
    def get(self):
        return ClienteModel.query.all()

    @blp.arguments(cliente_schema)
    @blp.response(201, cliente_schema)
    def post(self, data):
        if ClienteModel.query.filter_by(cpf=data["cpf"]).first():
            smorest_abort(409, message="CPF já cadastrado.")

        if data.get("email") and ClienteModel.query.filter_by(email=data["email"]).first():
            smorest_abort(409, message="Email já cadastrado.")

        novo = ClienteModel(**data)

        db.session.add(novo)
        db.session.commit()
        return novo


@blp.route("/<int:cliente_id>")
class Cliente(MethodView):

    @blp.response(200, cliente_schema)
    def get(self, cliente_id):
        return ClienteModel.query.get_or_404(cliente_id, "Cliente não encontrado.")

    def delete(self, cliente_id):
        cliente = ClienteModel.query.get_or_404(cliente_id, "Cliente não encontrado.")
        db.session.delete(cliente)
        db.session.commit()
        return jsonify({"message": "Cliente removido com sucesso!"})

    @blp.arguments(cliente_schema)
    @blp.response(200, cliente_schema)
    def put(self, data, cliente_id):

        cliente = ClienteModel.query.get_or_404(cliente_id, "Cliente não encontrado.")

        # Atualizações
        for campo, valor in data.items():
            setattr(cliente, campo, valor)

        db.session.commit()
        return cliente


api.register_blueprint(blp)


#@app.route("/") -- execução sem o tml
#def home():
#    return "<h1>API CRUD Clientes ativa! Acesse /swagger</h1>"
@app.route("/app")
def frontend():
    return send_from_directory("static", "index.html")

if __name__ == "__main__":
    app.run(debug=True)
