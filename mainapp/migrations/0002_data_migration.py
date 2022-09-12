from django.db import migrations


def forwards_func(apps, schema_editor):
    # Get model
    News = apps.get_model("mainapp", "News")
    # Create model's objects
    News.objects.create(
        title="Запуск нового курса по Python",
        preambule="Мы рады вам сообщить о запуске нового курса по Python для \
        начинающих!",
        body="Python предназначен для разработки и изучения новых приложений. \
        Мы предлагаем непросто изучить новый язык программирования, но и \
        научиться применять его на практике. Этот курс полезен не \
        только тем, кто хочет научиться программировать, но и всем тем, \
        кому не хватает времени на выполнение практических заданий, а также \
        тем, у кого нет возможности посещать курсы. Курс состоит из 7 \
        встреч — одно занятие в неделю длительностью 3 часа.\r\nВстречи \
        проводятся по воскресеньям с 14:00.",
    )
    News.objects.create(
        title="Урока по PHP в среду не состоится",
        preambule="Всем, кто не успел купить курс в понедельник, настоятельно \
        рекомендую это сделать по ссылке в конце публикации.",
        body="Сегодня в Саратове не будет проходить открытый урок по PHP, \
        который должен был состояться в среду на факультете компьютерных \
        наук СГУ. Преподавательница, за которой закреплена аудитория, \
        сказала что заболела и не придёт. На следующий урок, \
        запланированный на 28 февраля, перенесли всё, кроме курса \
        «Веб-программирование». Об этом сообщили в группе факультета в \
        социальной сети «ВКонтакте». Курс «Веб-программист» состоит из \
        двух частей. Первая — общий курс, идущий в течение 72 часов.",
    )
    News.objects.create(
        title="Всем руководителям подразделений подключится к Zoom",
        preambule="Все сотрудники подключены к Zoom, поэтому мы видим, что \
        они делают и говорят.",
        body="Каждый из 5 руководителей будет в одном из своих офисов с \
        использованием этого приложения. Мы хотим, чтобы они могли видеть всё, \
        что происходит на сайте, просматривать отчёты, которые им \
        предоставляются. После того как сотрудники подключили ZOOM, нам \
        важно, чтобы каждый секретарь, менеджер и прочие были \
        подключены ко всем 5 компьютерам.",
    )
    News.objects.create(
        title="Сегодня студенты всего мира отмечают праздник",
        preambule="Подробности — внутри...",
        body="Сегодня студенты всего мира отмечают праздник, который \
        официально признан международным, но более распространён в \
        Таких азиатских странах, как Китай или Япония. Он называется \
        Фестиваль студенческого пирога (Holly Fest) и празднуется каждый \
        год в начале сентября. Этот праздник объединяет студентов во \
        всём мире. Они отмечают начало нового учебного года и дарят \
        друг другу подарки. Во многих азиатских странах этот день также \
        знаменует начало нового года по китайскому календарю. День \
        Рождения: 9 июля, 23 года",
    )
    News.objects.create(
        title="Встречайте нового преподавателя направления DevOps",
        preambule="Дмитрий Шишмарёв работает в IT-бизнесе с 2001 года.",
        body="До прихода в компанию «1С-Битрикс» начинал карьеру в качестве \
        системного администратора. В 2009 перешёл на должность \
        DevOps-инженера, где и трудится по сей день, развиваясь в своей \
        сфере. Дмитрий — сертифицированный специалист компании \
        Bitrix. На его счету более 30 успешно реализованных проектов, \
        среди которых: разработка корпоративной системы управления \
        веб-проектами на базе 1C-Bitrix",
    )
    News.objects.create(
        title="JavaScript снова возглавил рейтинг самых отвратительных \
        языков",
        preambule="И опять, и снова.",
        body="Рейтинг самых отвратительных языков программирования, \
        составленный британским изданием, возглавляет JavaScript. В опросе \
        приняли участие более 1000 специалистов по разработке ПО, \
        работающих в различных компаниях. При составлении списка \
        учитывались такие свойства языка, как сложность и простота \
        обучения, а также производительность. Специалисты оценивали язык \
        по 10-балльной шкале, где один балл означал «ужасающий», а 10 \
        баллов — «отвратительный».",
    )


def reverse_func(apps, schema_editor):
    # Get model
    News = apps.get_model("mainapp", "News")
    # Delete objects
    News.objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [
        ("mainapp", "0001_initial"),
    ]
    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]
