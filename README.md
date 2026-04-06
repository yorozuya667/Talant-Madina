# Wedding invite starter for GitHub Pages

Внутри:
- `index.html` — сам сайт для GitHub Pages
- `.nojekyll` — чтобы GitHub Pages не лез в Jekyll
- `apps-script/Code.gs` — минимальный backend для записи `YES` в Google Sheets

## 1. Что должно быть в Google Sheets

Название листа:
`Guests`

Строка заголовков:
`token | guest_name | status | confirmed_at | link`

Пример:
`E3935D5188A9 | Гость1 | | |`

## 2. Что заменить в `apps-script/Code.gs`

Вставь ID своей таблицы:

```js
const SPREADSHEET_ID = 'PASTE_YOUR_GOOGLE_SHEET_ID_HERE';
```

## 3. Как задеплоить Apps Script

1. В Google Sheets: Extensions -> Apps Script
2. Вставь `Code.gs`
3. Deploy -> New deployment
4. Type: Web app
5. Execute as: Me
6. Who has access: Anyone
7. Deploy
8. Скопируй URL вида `https://script.google.com/macros/s/.../exec`

## 4. Что заменить в `index.html`

Найди:

`PASTE_YOUR_APPS_SCRIPT_WEBAPP_URL_HERE`

и вставь туда URL веб-приложения из Apps Script.

Если надо — отредактируй:
- имена пары
- дату
- время
- место
- адрес
- ссылку на карту
- `DEADLINE_ISO`

## 5. Как выложить на GitHub Pages

Лучше репозиторий назвать:
`yorozuya667.github.io`

Потом:
1. Загрузи `index.html` и `.nojekyll`
2. Settings -> Pages
3. Source: Deploy from a branch
4. Branch: main
5. Folder: / (root)

## 6. Формула персональных ссылок в Google Sheets

В `E2`:

```excel
=ARRAYFORMULA(ЕСЛИ(A2:A="";"";"https://yorozuya667.github.io/?t="&A2:A))
```

## 7. Что будет происходить

- гость открывает персональную ссылку
- нажимает кнопку
- браузер отправляет POST в Apps Script
- Apps Script ищет токен в таблице
- если токен найден и статус пустой — пишет `YES` и время
