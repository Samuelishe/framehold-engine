# PRODUCT_VISION

## Что такое Framehold Engine

Framehold Engine — self-hosted multi-user, multi-portfolio web gallery engine. Одна установка может хостить много независимых публичных фотопортфолио.

Framehold Engine — free and open-source software. Официальный проект распространяется бесплатно под AGPL-3.0-or-later; это не запрещает commercial use при соблюдении условий лицензии.

Пользователь сможет зарегистрироваться публично, подтвердить email, создать собственное Portfolio, выбрать curated visual theme, загрузить фотографии через приватный Framehold Dashboard, создать альбомы, настроить presentation options и опубликовать портфолио под публичным URL.

## Зачем он существует

Проект нужен как практический долгосрочный full-stack продукт для управляемой публикации фотоархива и портфолио. Он должен сохранять контроль над публичным UX, владельческой изоляцией, темами, медиа-презентацией и административными возможностями.

## Первые пользователи

Исходный личный сценарий остается важным:

- Irwyn;
- Polina;
- отец Irwyn.

Они являются первыми intended users, а не полной границей продукта.

## Целевое ощущение

Публичная часть должна восприниматься как premium personal photo portfolio или photo journal: спокойный интерфейс, сильная типографика, внимание к изображениям, аккуратная редакторская подача и хорошие mobile layouts.

## Основные роли

- Site Administrator — глобальный администратор установки.
- Portfolio Owner — зарегистрированный и email-verified пользователь, владеющий своим Portfolio.
- Public Visitor — посетитель, видящий только опубликованный non-suspended контент.

Возможная будущая роль Collaborator для совместного редактирования портфолио не входит в MVP.

## Не социальная сеть

Framehold Engine не является social network и не ориентирован на коммуникации.

MVP non-goals:

- no visitor comments;
- no likes;
- no follows;
- no public activity feed;
- no direct messages;
- no ratings;
- no public anonymous uploads;
- no social network mechanics;
- no mandatory social sharing buttons.

Текст у фотографии — это `caption` или author note, а не visitor comment.

## Долгосрочная кастомизация

- Несколько independent portfolios в одной установке.
- Curated themes с безопасными настройками.
- Theme-driven public presentation.
- Контролируемый viewer/lightbox.
- Управляемый показ captions, dates и allowlisted EXIF.
- Self-service Delete account and all data.
- Публичная философия без DRM: опубликованные фотографии viewable and saveable.
- Возможное расширение storage, search, tags, private albums и collaborator workflows позже.

## No DRM и пользовательские права

Framehold Engine не обещает защитить опубликованное изображение от копирования из браузера и не должен использовать fake copy protection. User-uploaded photographs не становятся AGPL-licensed автоматически; copyright остается у uploader или другого lawful rights holder.

## Почему это custom project

Готовые решения вроде WordPress, Piwigo, Lychee, Immich или PhotoPrism могут быть полезны как ориентиры, но они не являются выбранной основной архитектурой. Framehold Engine строится вокруг custom portfolio ownership, public registration, Framehold Dashboard, curated themes и server-rendered public presentation на Django/Wagtail.
