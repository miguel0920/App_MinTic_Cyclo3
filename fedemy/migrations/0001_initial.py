# Generated by Django 4.1.1 on 2022-10-05 00:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=15, unique=True, verbose_name='Username')),
                ('password', models.CharField(max_length=256, verbose_name='Password')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('createdatetime', models.DateTimeField(db_column='createdatetime')),
                ('updatedatetime', models.DateTimeField(db_column='updatedatetime', null=True)),
                ('isactive', models.BooleanField(db_column='isactive')),
                ('cityid', models.IntegerField(db_column='cityid', primary_key=True, serialize=False)),
                ('citycode', models.IntegerField(db_column='citycode')),
                ('cityname', models.CharField(db_column='cityname', max_length=255)),
            ],
            options={
                'db_table': 'cities',
            },
        ),
        migrations.CreateModel(
            name='Companies',
            fields=[
                ('createdatetime', models.DateTimeField(db_column='createdatetime')),
                ('updatedatetime', models.DateTimeField(db_column='updatedatetime', null=True)),
                ('isactive', models.BooleanField(db_column='isactive')),
                ('companyid', models.IntegerField(db_column='companyid', primary_key=True, serialize=False)),
                ('companyname', models.CharField(db_column='companyname', max_length=50)),
                ('companyaddress', models.CharField(db_column='companyaddress', max_length=50)),
                ('companyphone', models.CharField(db_column='companyphone', max_length=50)),
            ],
            options={
                'db_table': 'companies',
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('createdatetime', models.DateTimeField(db_column='createdatetime')),
                ('updatedatetime', models.DateTimeField(db_column='updatedatetime', null=True)),
                ('isactive', models.BooleanField(db_column='isactive')),
                ('orderid', models.IntegerField(db_column='orderid', primary_key=True, serialize=False)),
                ('ordernumber', models.CharField(db_column='ordernumber', max_length=100)),
                ('ordertotal', models.DecimalField(db_column='orderTotal', decimal_places=2, max_digits=5)),
                ('orderdatedelivery', models.DateField(db_column='orderdatedelivery', null=True)),
                ('usercreate', models.IntegerField(db_column='usercreate')),
                ('userupdate', models.IntegerField(db_column='userupdate', null=True)),
                ('cityid', models.ForeignKey(db_column='cityid', on_delete=django.db.models.deletion.DO_NOTHING, related_name='cityid_orders_set', to='fedemy.cities')),
            ],
            options={
                'db_table': 'orders',
            },
        ),
        migrations.CreateModel(
            name='PackageTypes',
            fields=[
                ('createdatetime', models.DateTimeField(db_column='createdatetime')),
                ('updatedatetime', models.DateTimeField(db_column='updatedatetime', null=True)),
                ('isactive', models.BooleanField(db_column='isactive')),
                ('packagetypeid', models.IntegerField(db_column='packagetypeid', primary_key=True, serialize=False)),
                ('packagetypename', models.CharField(db_column='packagetypename', max_length=50)),
            ],
            options={
                'db_table': 'packagetypes',
            },
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('createdatetime', models.DateTimeField(db_column='createdatetime')),
                ('updatedatetime', models.DateTimeField(db_column='updatedatetime', null=True)),
                ('isactive', models.BooleanField(db_column='isactive')),
                ('personid', models.IntegerField(db_column='personid', primary_key=True, serialize=False)),
                ('personfirstname', models.CharField(db_column='personfirstname', max_length=50)),
                ('personsecondname', models.CharField(db_column='personsecondname', max_length=50, null=True)),
                ('personlastname', models.CharField(db_column='personlastname', max_length=50)),
                ('personrsecondlastname', models.CharField(db_column='personrsecondlastname', max_length=50)),
                ('personaddress', models.CharField(db_column='personaddress', max_length=50)),
                ('personphone', models.CharField(db_column='personphone', max_length=50)),
                ('personemail', models.CharField(db_column='personemail', max_length=50)),
                ('persondocumentnumber', models.CharField(db_column='persondocumentnumber', max_length=50)),
            ],
            options={
                'db_table': 'people',
            },
        ),
        migrations.CreateModel(
            name='States',
            fields=[
                ('createdatetime', models.DateTimeField(db_column='createdatetime')),
                ('updatedatetime', models.DateTimeField(db_column='updatedatetime', null=True)),
                ('isactive', models.BooleanField(db_column='isactive')),
                ('stateid', models.IntegerField(db_column='stateid', primary_key=True, serialize=False)),
                ('statename', models.CharField(db_column='statename', max_length=50)),
                ('statecode', models.IntegerField(db_column='statecode')),
            ],
            options={
                'db_table': 'states',
            },
        ),
        migrations.CreateModel(
            name='StatesOrders',
            fields=[
                ('createdatetime', models.DateTimeField(db_column='createdatetime')),
                ('updatedatetime', models.DateTimeField(db_column='updatedatetime', null=True)),
                ('isactive', models.BooleanField(db_column='isactive')),
                ('stateorderid', models.IntegerField(db_column='stateorderid', primary_key=True, serialize=False)),
                ('stateordername', models.CharField(db_column='stateordername', max_length=50)),
            ],
            options={
                'db_table': 'statesorders',
            },
        ),
        migrations.CreateModel(
            name='UserCompanies',
            fields=[
                ('createdatetime', models.DateTimeField(db_column='createdatetime')),
                ('updatedatetime', models.DateTimeField(db_column='updatedatetime', null=True)),
                ('isactive', models.BooleanField(db_column='isactive')),
                ('usercompanyid', models.IntegerField(db_column='usercompanyid', primary_key=True, serialize=False)),
                ('companyid', models.ForeignKey(db_column='companyid', on_delete=django.db.models.deletion.CASCADE, related_name='usercompanies', to='fedemy.companies')),
                ('fedemy_userid', models.ForeignKey(db_column='fedemy_userid', on_delete=django.db.models.deletion.CASCADE, related_name='fedemy_user', to=settings.AUTH_USER_MODEL)),
                ('personid', models.ForeignKey(db_column='personid', on_delete=django.db.models.deletion.CASCADE, related_name='People', to='fedemy.people')),
            ],
            options={
                'db_table': 'usercompanies',
            },
        ),
        migrations.CreateModel(
            name='Packages',
            fields=[
                ('createdatetime', models.DateTimeField(db_column='createdatetime')),
                ('updatedatetime', models.DateTimeField(db_column='updatedatetime', null=True)),
                ('isactive', models.BooleanField(db_column='isactive')),
                ('packageid', models.BigIntegerField(db_column='packageid', primary_key=True, serialize=False)),
                ('packagedescription', models.CharField(db_column='packagedescription', max_length=50)),
                ('packagetitle', models.CharField(db_column='packagetitle', max_length=50)),
                ('packageprice', models.DecimalField(db_column='packageprice', decimal_places=2, max_digits=11)),
                ('packagequantity', models.IntegerField(db_column='packagequantity')),
                ('packagetypeid', models.ForeignKey(db_column='packagetypeid', on_delete=django.db.models.deletion.CASCADE, related_name='packagetypeid_packeage_set', to='fedemy.packagetypes')),
                ('usercompanyid', models.ForeignKey(blank=True, db_column='usercompanyid', on_delete=django.db.models.deletion.CASCADE, to='fedemy.usercompanies')),
            ],
            options={
                'db_table': 'packages',
            },
        ),
        migrations.CreateModel(
            name='OrdersDetails',
            fields=[
                ('createdatetime', models.DateTimeField(db_column='createdatetime')),
                ('updatedatetime', models.DateTimeField(db_column='updatedatetime', null=True)),
                ('isactive', models.BooleanField(db_column='isactive')),
                ('orderdetailid', models.IntegerField(db_column='orderdetailid', primary_key=True, serialize=False)),
                ('orderdetailquantity', models.IntegerField(db_column='orderdetailquantity')),
                ('orderdetailprice', models.DecimalField(db_column='orderdetailprice', decimal_places=2, max_digits=11)),
                ('orderid', models.ForeignKey(db_column='orderid', on_delete=django.db.models.deletion.DO_NOTHING, related_name='orderid_ordersdetails_set', to='fedemy.orders')),
                ('packageid', models.ForeignKey(db_column='packageid', on_delete=django.db.models.deletion.DO_NOTHING, related_name='packageid_ordersdetails_set', to='fedemy.packages')),
            ],
            options={
                'db_table': 'ordersdetails',
            },
        ),
        migrations.AddField(
            model_name='orders',
            name='personreceiverid',
            field=models.ForeignKey(db_column='personreceiverid', on_delete=django.db.models.deletion.DO_NOTHING, related_name='personreceiverid_orders_set', to='fedemy.people'),
        ),
        migrations.AddField(
            model_name='orders',
            name='personsenderid',
            field=models.ForeignKey(db_column='personsenderid', on_delete=django.db.models.deletion.DO_NOTHING, related_name='personsenderid_orders_set', to='fedemy.people'),
        ),
        migrations.AddField(
            model_name='orders',
            name='stateorderid',
            field=models.ForeignKey(db_column='stateorderid', on_delete=django.db.models.deletion.DO_NOTHING, related_name='stateOrderId_orders_set', to='fedemy.statesorders'),
        ),
        migrations.AddField(
            model_name='orders',
            name='usercompanyid',
            field=models.ForeignKey(db_column='usercompanyid', on_delete=django.db.models.deletion.DO_NOTHING, related_name='usercompanyid_orders_set', to='fedemy.usercompanies'),
        ),
        migrations.AddField(
            model_name='cities',
            name='stateid',
            field=models.ForeignKey(db_column='stateid', on_delete=django.db.models.deletion.DO_NOTHING, related_name='stateid_states_set', to='fedemy.states'),
        ),
    ]
