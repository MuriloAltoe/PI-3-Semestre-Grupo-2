<?php

use Illuminate\Database\Migrations\Migration;
use Jenssegers\Mongodb\Schema\Blueprint;
use Illuminate\Support\Facades\Mongo;

class Banco extends Migration
{
    /**
     * Run the migrations.
     */
    public function up(): void
    {
        Schema::connection('mongodb')->create('usuario', function (Blueprint $collection) {
            $collection->index('_id');
            $collection->index('id');
            $collection->string('nome');
            $collection->string('email')->unique();
            $collection->string('senha');
            $collection->boolean('produtor');
            $collection->boolean('entrega');
            $collection->json('contato');
            $collection->timestamps();
        });

        Schema::connection('mongodb')->create('barraca', function (Blueprint $collection) {
            $collection->index('_id');
            $collection->string('descricao');
            $collection->integer('id_produtos')->unique();
            $collection->string('endereco');
            $collection->array('metodos-pagamento');
            $collection->timestamps();
        });

        Schema::connection('mongodb')->create('produtos', function (Blueprint $collection) {
            $collection->index('_id');
            //$collection->intval('id')->unique();
            $collection->string('descricao');
            $collection->doubleval('preco');
            $collection->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::connection('mongodb')->drop('usuario');
        Schema::connection('mongodb')->drop('barraca');
        Schema::connection('mongodb')->drop('produto');

    }
};
