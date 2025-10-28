from django.db import migrations, models
import django.db.models.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('category', models.CharField(choices=[('breakfast', 'Breakfast'), ('lunch', 'Lunch'), ('snacks', 'Snacks'), ('desserts', 'Desserts'), ('beverages', 'Beverages')], max_length=20)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, validators=[django.db.models.validators.MinValueValidator(0)])),
                ('image_url', models.URLField(blank=True, null=True)),
                ('is_available', models.BooleanField(default=True)),
                ('rating', models.FloatField(default=4.5, validators=[django.db.models.validators.MinValueValidator(0)])),
                ('reviews_count', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=20, unique=True)),
                ('customer_name', models.CharField(max_length=100)),
                ('table_number', models.IntegerField()),
                ('phone_number', models.CharField(max_length=15)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('preparing', 'Preparing'), ('ready', 'Ready'), ('completed', 'Completed'), ('cancelled', 'Cancelled')], default='pending', max_length=20)),
                ('payment_method', models.CharField(choices=[('online', 'Online Payment'), ('cod', 'Cash on Delivery')], max_length=20)),
                ('payment_status', models.CharField(default='pending', max_length=20)),
                ('special_instructions', models.TextField(blank=True, null=True)),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.db.models.validators.MinValueValidator(0)])),
                ('tax', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.db.models.validators.MinValueValidator(0)])),
                ('delivery_charge', models.DecimalField(decimal_places=2, default=0, max_digits=10, validators=[django.db.models.validators.MinValueValidator(0)])),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.db.models.validators.MinValueValidator(0)])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', models.CharField(max_length=100, unique=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_method', models.CharField(max_length=20)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed'), ('failed', 'Failed'), ('refunded', 'Refunded')], default='pending', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='payment', to='canteen.order')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(validators=[django.db.models.validators.MinValueValidator(1)])),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('menu_item', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='canteen.menuitem')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='canteen.order')),
            ],
        ),
    ]
