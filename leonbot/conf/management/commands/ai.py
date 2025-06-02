import os

from django.core.management.base import BaseCommand
from django.conf import settings

from transformers import (
	GPT2Tokenizer,
	GPT2LMHeadModel,
	Trainer,
	TrainingArguments,
	DataCollatorForLanguageModeling,
)
from datasets import load_dataset

from ....conf.validators import validate_ai_paths



class Command(BaseCommand):

	def add_arguments(self, parser):
		parser.add_argument(
			'--train',
			action='store_true',
		)

	def handle(self, *args, **options):

		self.stdout.write("Strat Validate Path Adrs...")
		GPT2_TOKENNIZER_PATH: str = settings.GPT2_TOKENNIZER_PATH
		GPT2_LMHEADMODEL_PATH: str = settings.GPT2_LMHEADMODEL_PATH
		AI_TEXT_TRAIN_PATH: str = settings.AI_TEXT_TRAIN_PATH
		output_dir = os.path.join(settings.PROJECT_ROOT, "aimodel")

		validate_ai_paths(
			output_dir,
			GPT2_TOKENNIZER_PATH, GPT2_LMHEADMODEL_PATH, AI_TEXT_TRAIN_PATH
		)

		self.stdout.write("is valid paths...")
		self.stdout.write("AI Model Strat for Training...")

		tokenizer = GPT2Tokenizer.from_pretrained(GPT2_TOKENNIZER_PATH)
		model = GPT2LMHeadModel.from_pretrained(GPT2_LMHEADMODEL_PATH)

		tokenizer.pad_token = tokenizer.eos_token
		model.resize_token_embeddings(len(tokenizer))


		dataset = load_dataset(
			"text",
			data_files={"train": AI_TEXT_TRAIN_PATH},
		)

		def tokenize_func(exple):
			return tokenizer(exple["text"], truncation=True, max_length=128, padding="max_length")

		tokenized_datasets = dataset.map(tokenize_func, batched=True, remove_columns=["text"])

		data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)

		training_args = TrainingArguments(
			output_dir=output_dir,
			overwrite_output_dir=True,
			num_train_epochs=3,
			per_device_train_batch_size=4,
			save_steps=500,
			save_total_limit=2,
			logging_steps=100,
		)

		trainer = Trainer(
			model=model,
			args=training_args,
			data_collator=data_collator,
			train_dataset=tokenized_datasets["train"],
		)

		trainer.train()
