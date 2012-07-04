class CreateFilms < ActiveRecord::Migration
  def change
    create_table :films do |t|
      t.text :title

      t.timestamps
    end
  end
end
