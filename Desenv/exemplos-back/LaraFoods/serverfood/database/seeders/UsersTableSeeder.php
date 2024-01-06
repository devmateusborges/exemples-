<?php

namespace Database\Seeders;

use App\Models\{
    Tenant,
    User
};
use Illuminate\Database\Seeder;

class UsersTableSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
        $tenant = Tenant::first();

        $tenant->users()->create([
            'name' => 'admin',
            'email' => 'admin@admin.com.br',
            'password' => bcrypt('123456'),
        ]);
    }
}
