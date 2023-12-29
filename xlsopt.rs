extern crate rust_excel;
use rust_excel::read_excel;

fn main() {
    let file_path = "path/to/your/excel.xlsx";
    let sheet_name = "Sheet1";
    let data = read_excel(file_path, sheet_name).unwrap();
    println!("{:?}", data);
}

