# Generated by Django 2.2.6 on 2020-01-17 02:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Canned',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(max_length=10)),
                ('c_mes', models.CharField(max_length=50)),
                ('c_dai', models.CharField(max_length=20)),
                ('c_spa', models.CharField(max_length=10)),
                ('c_grow', models.CharField(max_length=10)),
                ('c_cou', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Cloud',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(max_length=10)),
                ('c_quire', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Evil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('e_name', models.CharField(max_length=10)),
                ('e_take', models.CharField(max_length=10)),
                ('e_det', models.CharField(max_length=30)),
                ('e_note', models.CharField(max_length=20)),
                ('e_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Fore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Gods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('g_name', models.CharField(max_length=10)),
                ('g_sex', models.CharField(max_length=10)),
                ('g_age', models.CharField(max_length=10)),
                ('g_town', models.CharField(max_length=10)),
                ('g_easy', models.CharField(max_length=10)),
                ('gc_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tiantingapp.Cloud')),
                ('gf_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tiantingapp.Fore')),
            ],
        ),
        migrations.CreateModel(
            name='Icm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('i_name', models.CharField(max_length=10)),
                ('i_url', models.CharField(max_length=100, null=True)),
                ('ii_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tiantingapp.Icm')),
            ],
        ),
        migrations.CreateModel(
            name='Lite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('l_name', models.CharField(max_length=10)),
                ('l_dist', models.CharField(max_length=10)),
                ('l_fore', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Ory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('o_name', models.CharField(max_length=10)),
                ('o_arts', models.CharField(max_length=10)),
                ('o_mark', models.CharField(max_length=20)),
                ('o_exe', models.CharField(max_length=10)),
                ('o_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Power',
            fields=[
                ('primary_key', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('p_name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('r_name', models.CharField(max_length=10)),
                ('r_grade', models.CharField(max_length=10)),
                ('r_jury', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Sure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_name', models.CharField(max_length=20)),
                ('s_mend', models.CharField(max_length=50)),
                ('s_cou', models.CharField(max_length=10)),
                ('s_adr', models.CharField(max_length=10)),
                ('s_exif', models.CharField(max_length=10)),
                ('s_favor', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Worn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('w_name', models.CharField(max_length=10)),
                ('w_bou', models.CharField(max_length=10)),
                ('w_yed', models.CharField(max_length=10)),
                ('w_ect', models.CharField(max_length=50)),
                ('w_acre', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Yeah',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('y_name', models.CharField(max_length=10)),
                ('y_vxi', models.CharField(max_length=10)),
                ('y_aes', models.CharField(max_length=10)),
                ('y_evd', models.CharField(max_length=10)),
                ('y_fbe', models.CharField(max_length=10)),
                ('yg_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tiantingapp.Gods')),
            ],
        ),
        migrations.CreateModel(
            name='Touch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_name', models.CharField(max_length=20)),
                ('t_pass', models.CharField(max_length=10)),
                ('t_mail', models.CharField(max_length=20)),
                ('t_iphone', models.CharField(max_length=20)),
                ('t_vat', models.BooleanField(default=False)),
                ('tc_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tiantingapp.Cloud')),
                ('tf_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tiantingapp.Fore')),
                ('tg_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tiantingapp.Gods')),
                ('tr_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tiantingapp.Role')),
            ],
        ),
        migrations.CreateModel(
            name='Rwt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('r_name', models.CharField(max_length=10)),
                ('r_mes', models.CharField(max_length=50)),
                ('r_spa', models.CharField(max_length=10)),
                ('r_grow', models.CharField(max_length=10)),
                ('rr_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tiantingapp.Rwt')),
            ],
        ),
        migrations.CreateModel(
            name='Quin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q_name', models.CharField(max_length=10)),
                ('q_thing', models.CharField(max_length=30)),
                ('q_cti', models.CharField(max_length=10)),
                ('qg_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tiantingapp.Gods')),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m_name', models.CharField(max_length=10)),
                ('m_handle', models.CharField(max_length=6)),
                ('m_care', models.CharField(max_length=20)),
                ('mi_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tiantingapp.Icm')),
                ('mr_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tiantingapp.Role')),
            ],
        ),
        migrations.CreateModel(
            name='Dies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d_name', models.CharField(max_length=10)),
                ('d_rate', models.CharField(max_length=10)),
                ('d_dist', models.CharField(max_length=10)),
                ('dc_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tiantingapp.Canned')),
                ('dr_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tiantingapp.Rwt')),
            ],
        ),
        migrations.AddField(
            model_name='cloud',
            name='cf_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tiantingapp.Fore'),
        ),
        migrations.CreateModel(
            name='Ation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_name', models.CharField(max_length=10)),
                ('a_names', models.CharField(max_length=10)),
                ('ar_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tiantingapp.Role')),
                ('at_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tiantingapp.Touch')),
            ],
        ),
    ]