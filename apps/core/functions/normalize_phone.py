def normalize_phone(raw_phone: str) -> str:
	normalized_phone = ''.join(x for x in raw_phone if x.isdigit())

	if normalized_phone:

		if normalized_phone.startswith('8'):
			normalized_phone = f'7{normalized_phone[1:]}'

		normalized_phone = f'+{normalized_phone}'

	return normalized_phone
