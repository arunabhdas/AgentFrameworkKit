// Learn more about Tauri commands at https://tauri.app/develop/calling-rust/

use tauri::{AppHandle};
use tauri::Emitter;

#[tauri::command]
fn greet(app:AppHandle, name: &str) -> String {
    app.emit("event_name", "eventpayload").unwrap();
    format!("Hello, {}! You've been greeted from Rust!", name)
}

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
    tauri::Builder::default()
        .plugin(tauri_plugin_opener::init())
        .invoke_handler(tauri::generate_handler![greet])
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
